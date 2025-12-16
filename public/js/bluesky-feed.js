class BlueSkyFeedWidget {
    constructor(config) {
        // Configuration with defaults
        this.handle = config.handle || 'YOUR_HANDLE.bsky.social';
        this.hashtag = config.hashtag || 'YOUR_HASHTAG';
        this.limit = config.limit || 5;
        this.container = document.getElementById('bluesky-posts');
        this.loadingElement = document.querySelector('.loading');
        
        console.log('Widget initialized');
        console.log('Container found:', !!this.container);
        console.log('Loading element found:', !!this.loadingElement);
        
        this.init();
    }

    async init() {
        try {
            await this.fetchPosts();
        } catch (error) {
            this.showError('Failed to load posts. Please try again later.');
            console.error('BlueSky feed error:', error);
        }
    }

    async fetchPosts() {
        console.log('Fetching posts for handle:', this.handle);
        
        // Try the public Bluesky API endpoint (no auth required)
        const apiUrl = `https://public.api.bsky.app/xrpc/app.bsky.feed.getAuthorFeed?actor=${this.handle}&limit=50`;
        
        console.log('API URL:', apiUrl);
        
        try {
            const response = await fetch(apiUrl, {
                method: 'GET',
                headers: {
                    'Accept': 'application/json',
                },
            });
            console.log('Response status:', response.status);
            
            if (!response.ok) {
                console.log('Public API failed, trying alternative...');
                await this.fetchPostsAlternative();
                return;
            }

            console.log('About to parse JSON...');
            const data = await response.json();
            console.log('JSON parsed successfully');
            console.log('API response:', data);
            console.log('Feed exists:', !!data.feed);
            console.log('Feed length:', data.feed ? data.feed.length : 'undefined');
            console.log('About to process posts...');
            
            this.processPosts(data.feed || []);
            console.log('processPosts completed');
            
        } catch (error) {
            console.error('Fetch error:', error);
            await this.fetchPostsAlternative();
        }
    }

    async fetchPostsAlternative() {
        try {
            const profileUrl = `https://public.api.bsky.app/xrpc/app.bsky.actor.getProfile?actor=${this.handle}`;
            console.log('Trying profile API:', profileUrl);
            
            const profileResponse = await fetch(profileUrl);
            console.log('Profile response status:', profileResponse.status);
            
            if (profileResponse.ok) {
                const profileData = await profileResponse.json();
                console.log('Profile data:', profileData);
                this.showProfileInfo(profileData);
            } else {
                throw new Error('Could not access profile');
            }
        } catch (error) {
            console.error('Alternative fetch error:', error);
            this.showError('Unable to load posts. This might be due to privacy settings or API limitations.');
        }
    }

    processPosts(feed) {
        try {
            console.log('=== PROCESSING POSTS ===');
            console.log('Feed array length:', feed.length);
            
            if (feed.length > 0) {
                console.log('First post sample:', feed[0]);
            }
            
            let filteredPosts;
            
            // Check if we have placeholder values
            if (this.hashtag === 'YOUR_HASHTAG' || !this.hashtag) {
                console.log('No hashtag filter - showing all posts');
                filteredPosts = feed.slice(0, this.limit);
            } else {
                console.log('Filtering by hashtag:', this.hashtag);
                const hashtagLower = this.hashtag.toLowerCase();
                filteredPosts = feed.filter(item => {
                    const post = item.post;
                    if (!post.record || !post.record.text) return false;
                    
                    const text = post.record.text.toLowerCase();
                    const hasHashtag = text.includes(`#${hashtagLower}`);
                    if (hasHashtag) {
                        console.log('Found hashtag in post:', post.record.text.substring(0, 100));
                    }
                    return hasHashtag;
                }).slice(0, this.limit);
            }

            console.log('Filtered to', filteredPosts.length, 'posts');

            this.hideLoading();

            if (filteredPosts.length === 0) {
                console.log('No posts to display - calling showEmpty');
                this.showEmpty();
                return;
            }

            console.log('Calling renderPosts with', filteredPosts.length, 'posts');
            this.renderPosts(filteredPosts);
            console.log('renderPosts completed');
            
        } catch (error) {
            console.error('Error in processPosts:', error);
            this.hideLoading();
            this.showError('Error processing posts: ' + error.message);
        }
    }

    renderPosts(posts) {
        console.log('=== RENDERING POSTS ===');
        try {
            const renderedHTML = posts.map(item => {
                const post = item.post;
                const createdAt = new Date(post.record.createdAt);
                const formattedDate = this.formatDate(createdAt);
                
                // Highlight hashtags in the text
                const highlightedText = this.highlightHashtags(post.record.text);
                
                // Get engagement stats
                const likeCount = post.likeCount || 0;
                const repostCount = post.repostCount || 0;
                const replyCount = post.replyCount || 0;

                return `
                    <div class="bluesky-post">
                        <div class="post-content">${highlightedText}</div>
                        <div class="post-meta">
                            <span class="post-date">${formattedDate}</span>
                            <div class="post-stats">
                                ${replyCount > 0 ? `<span class="stat">💬 ${replyCount}</span>` : ''}
                                ${repostCount > 0 ? `<span class="stat">🔄 ${repostCount}</span>` : ''}
                                ${likeCount > 0 ? `<span class="stat">❤️ ${likeCount}</span>` : ''}
                            </div>
                        </div>
                    </div>
                `;
            }).join('');

            console.log('Generated HTML length:', renderedHTML.length);
            this.container.innerHTML = renderedHTML;
            console.log('HTML inserted into container');
            
        } catch (error) {
            console.error('Error in renderPosts:', error);
            this.showError('Error rendering posts: ' + error.message);
        }
    }

    highlightHashtags(text) {
        const escaped = text
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#39;');
        
        return escaped.replace(/#(\w+)/g, '<span class="hashtag">#$1</span>');
    }

    formatDate(date) {
        const now = new Date();
        const diffMs = now - date;
        const diffMins = Math.floor(diffMs / 60000);
        const diffHours = Math.floor(diffMs / 3600000);
        const diffDays = Math.floor(diffMs / 86400000);

        if (diffMins < 1) return 'now';
        if (diffMins < 60) return `${diffMins}m`;
        if (diffHours < 24) return `${diffHours}h`;
        if (diffDays < 7) return `${diffDays}d`;
        
        return date.toLocaleDateString();
    }

    hideLoading() {
        if (this.loadingElement) {
            this.loadingElement.style.display = 'none';
        }
    }

    showError(message) {
        this.hideLoading();
        this.container.innerHTML = `<div class="error-message">${message}</div>`;
    }

    showEmpty() {
        const message = (this.hashtag === 'YOUR_HASHTAG' || !this.hashtag) 
            ? 'Configure your hashtag in bluesky-feed.js to filter posts'
            : `No posts found with hashtag #${this.hashtag}`;
            
        this.container.innerHTML = `
            <div class="empty-message">
                ${message}
            </div>
        `;
    }

    showProfileInfo(profile) {
        this.hideLoading();
        this.container.innerHTML = `
            <div class="empty-message">
                <p>Found profile: <strong>${profile.displayName || profile.handle}</strong></p>
                <p>Posts may not be publicly accessible or require authentication.</p>
                <p>Try making your posts public in your Bluesky settings.</p>
            </div>
        `;
    }
}

// Initialize the widget when the page loads
document.addEventListener('DOMContentLoaded', function() {
    new BlueSkyFeedWidget({
        handle: 'joshafairhead.bsky.social',
        hashtag: 'YOUR_HASHTAG',
        limit: 1
    });
});