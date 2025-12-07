+++
authors = ["Josh Fairhead"]
title = "Research Methods: Bibliography"
description = "Bibliography and reading around subject area"
draft = true

[taxonomies]
tags = ["Audio"]
[extra]
featured = true
banner = "cover.jpg"
hero = false
+++

<!--- 

TODO: Add pngs of the bibliography and feedback.

--->

# PG Research Methods - Assignment 3 ʻBibliographyʼ


## Introduction
In preparation for the upcoming proposal this bibliography is based around the subjective musicality of various distortions, defined as any change from an input signal to output signal. 

There are two main headings that help categorise various distortions; linear and non-linear. Linear distortion is a resultant change to the amplitude and/or phase spectrum of a signal that does not introduce additional frequency components. Non-linear distortion is when additional frequency components are added to the spectrum, they may or may not be related to the amplitude/frequency of the original signal. However if the non-linearity lacks an identifiable relationship with the input signal it is typically referred to as noise rather than 'non-linear distortion'.

Both these distortions usually occur at different stages of signal processing and so a single piece of equipment will usually exhibit both linear and non-linear distortions; it is their relationships that becomes 'musical'. The critical question posed is: how do we re-create what we define as musical when its a subjective quantifier? From research its understood that different distortions have different subjective responses which are quantifiable, however its the relation of all these distortions thats important if we are to gauge 'musicality'.

The available literature is quite extensive about the audible perception of linear/non-linear distortion, however there is only a little work available relating the subjective perception to our cognition of music, and so this bibliography will contain many books/papers concerned with these subjects individually.

## Notes
• Bibliography is arranged alphabetically by title.
• Bibliography is divided into papers, articles and books.
• Interdisciplinary sources are numerous so a list is included in alphabetical order of title, as opposed to sources titled under one large category.
• Further reading is included after interdisciplinary source list.

## Bibliography
Barbati, S. (unknown) *A Perceptual Approach on Clipping and Saturation* – Simulanalog, [online:
http://www.simulanalog.org/, accessed 07/12/10].

The subjective response to clipping and saturation is discussed by Barbati in this paper. The properties of symmetric and asymmetric clipping along with the intermodulation distortion as a result of each is examined. Here it is shown that even harmonics produce more musically consonant side bands than odd harmonics. A processing chain to reduce the DC current from asymmetric limiting is also suggested; if an instantaneous amplitude above a threshold is clipped filtered and clipped again the DC is reduced, Barbati claims that this double distortion process doesn't create extra acoustic artefacts and increases clarity in the low end as it would otherwise be masked.

Geddes & Lee (2006)* Audibility of Linear Distortion with Variations in Sound Pressure Level and Group Delay* – AES eJournal, paper 6888.

This work follows Geddes & Lees 2003 paper on the Auditory Perception of Nonlinear Distortion, explaining that the perceived response to linear distortion is dependant on level intensity is greatly effected by our non-linear hearing mechanisms. This has implications on the perception of non linear distortion; our non-linear hearing makes it difficult to distinguish a subjective response between non-linearities in the audio or the ear. Its is important to understand differences between non-linearities in order to hypothesise about the musical perception of such distortions.

Cabot, R. (1990) Audible Effects vs. Objective Measurements in the Electrical Signal Path - AES
ejournal, paper 8-008.

This paper gives an introduction into linear/non-linear distortion, discussing factors that effect its audibility as well as the difficulty in quantifying what is heard on 'perceptual' scale. The subject matter of this paper is almost symbiotic with the perception of musicality, if a piece of hardware has distorts, but not audibly, how can it be musical?

Geddes & Lee (2003) *Auditory Perception of Nonlinear Distortion; Theory* – AES eJournal, paper 5890.

This is the preliminary theory paper to the authors other paper carrying the same title (below). It explains about the masking effects of high order distortion on our perception of lower order distortions. The main point of the paper is that a systems non-linear response can be summed from underlying linear transfer functions; an easy way to think of this is to picture chaos theory in the audio world, everything is a consequence of mappable actions that can be summed up into a source equation.

Geddes & Lee (2003) *Auditory Perception of Nonlinear Distortion* – AES eJournal, paper 5891.

In this paper a Geddes & Lee present a proposed metric for measuring non-linear distortion with correlation to a perceptual scale, this paper explains the proposed metric also providing evidence that it works through predicting the experiment results. Essentially the paper demonstrates that our perception of distortion is based on the underlying transfer function of a system rather than the typical spectral approaches used such as THD values.

Serafini, T. (unknown) *A Perceptual Approach to Equalisation* – Simulanalog, [online: http://www.simulanalog.org/, accessed 07/12/10].

This article is about filter design in the digital domain, with reference to analog design. This article explains the types of non linearities inherent in analog filter design and suggests that the best way to emulate these is to either use a static nonlinear transfer function such as waveshaper or to use dynamic coefficients to emulate the non-linearities found throughout the signal chain such as resistance in passive components, inductance, etc. Serafini feels that the relationship between the filter coefficients and their interaction is what makes a filter 'musical'.

Toulson, R. (2008) *Can We Fix It? – The consequences of ‘fixing it in the mix’ with common equalisation techniques are scientifically evaluated* – Art of Record Production eJournal, Issue 3.

This paper evaluates the scientific merit of fixing something at mix stage and argues strongly that source signals should be as close to the final product as possible. Toulson then discusses digital filters and their musical effect; of particular interest in the part about an equalisers effect on an instruments harmonic profile (Timbre). An interesting idea that arose from this paper is that if we could alter the harmonic profile in a controlled way and apply a power distribution in a pleasant manner, we could create more musical timbres that perceptually make instruments sound better; this is essentially saturation however finding a subjectively pleasant power distribution is another task.

Orfandis, S. (1997) *Digital Parametric Equalizer Design with Prescribed Nyquist-Frequency Gain* – AES eJournal, paper 8679.

In this paper Orfandis discusses the problems with two pole filters; at high frequencies and band width we get a sharper roll off near the Nyquist frequency as a result of their bilinear design. Here a new method is proposed in order to closer replicate the response of an analog filter when approaching the Nyquist frequency. This is done by freeing the Nyquist frequency gain coefficient allowing digital equalisers more closely emulate an analogue slope closer to Nyquist. This paper highlights an interesting approach in designing more musical filters. 

Irwin, M. (2009) *Distortion and Subjective Audio Quality* – Art of Record Production eJournal, not issued.

This paper is focused on the linear and non-linear distortions found in various processes throughout the signal chain in both analog and digital equipment; also presenting subjective views on these distortions. This paper is interesting because the subjective views are essentially labelling distortions as musical or unmusical; from other papers it has been shown that examining relationships between the musical distortions and music theory can perhaps provide a quantifiable reason for certain subjective views.

Yeh, D. (2009) *Digital Implementation of Musical Distortion Circuits By Analysis and Simulation* – Doctoral Dissertation for Stanford University.

This paper describes the musical effects of distortions incurred along electronic signal paths, it describes how they are formed and discusses implementation in the digital realm using finite impulse response filters with coefficients derived from electronic test models. This equates to copying the musical aspects of equipment in existence and if this approach can be modified algorithmically so that the coefficients are adapted from a perceptual model, we could create much more pleasing results.

Gan & Oo (2008) *Harmonic and Intermodulation Analysis of Nonlinear Devices Used in Virtual Bass Systems* – AES eJournal, paper 7403.

The focus of this paper is on generating harmonic interval (intermodulation) distortion in higher frequencies psycho-acoustically tricking our brains into perceiving bass frequencies that don't exist on band limited playback systems. This is interesting because it outlines the intermodulation distortion needed to perceptually hear these frequencies especially as they are musically related through an 'interharmonic analysis formula'. It is another example of our perception being based on musical rules.

Langevin, R. (1963) *Intermodulation Distortion in Tape Recorders* – AES Journal, Volume 11, Issue 3.

Intermodulation in relation to music theory is discussed by Langevin in this paper. He shows that intermodulation frequencies aren't necessarily dissonant and that they often correspond with to harmonious frequencies. Langevin at one point even states 'It therefore follows that if the music is harmonious there is a good chance will be harmonious and not too noticeable'. He also talks about even and odd harmonics and their inter-modulated relationship with reference music theory.

Cabot, R. (1978) *Measurement of Audio Slew Rate* – AES eJournal, paper 1414.

Slew rate is a form of transient intermodulation distortion that is proportional to frequency, its maximum rate is derived from a phase shift of frequencies where all frequencies pass through zero at the same time. This causes a piece of equipment to over shoot its destination adding non-linear distortion. In this paper Cabot points to asymmetry being inherent in musical sounds and therefore more likely to sound musical.

Hideo et al. (1980) *On the perception of Phase Distortion* – AES Journal, Volume 28, Issue 11.

The subject of our perception of phase distortion in filters is broached by Hideo et al. It is an earlier examination of the audibility of minute timing offsets of the component waves in a signal. The conclusion is that they are audible but by how much is an individual ability. Presumably this would be some listeners sensitivity to amplitude changes as component waveforms interact with each other. This phase relationship defines the complex non-linearities found in equipment and is a second dimension to the musicality of a piece of equipments on top of frequency response.

Fletcher, T. (2009) *Recording in The World* – Art of Record Production eJournal, not issued.

Here the topic discussed is the distortions that occur in our non-linear hearing in relationship to recording equipment design. Fletcher talks about the hearing mechanism and how frequencies out side of the hearing range can effect our perception also, he also talks about current digital filter design and how detrimental they are to phase relationships. In a digital environment its important to note that frequencies cannot extend above the Nyquist limit, however as processing power increases and higher sample rates become more common this barrier will disappear. As digital processing becomes more accurate (with less initial phase shifts) we will be able to closer replicate the analogue complexity in order to make digital processing sound perceptually more 'musical'. 

Tzur & Colloms (1999) *The Effect of MaxxBass Psychoacoustic Bass Enhancement on Loudspeaker Design* – AES eJournal, paper 4892.

This paper explains that the MaxxBass enhancer works by splitting the signal into two pass bands around the third harmonic. The low frequencies are used to generate a weighted series of higher harmonics/intermodulation distortion. This distortion is used to stimulate an auditory sensation at the original loudness/pitch of the fundamental, at this point the fundamental is filtered out and the harmonics are introduced into the higher pass band. This makes use of the missing fundamental phenomena where the intermodulation distortion makes our brains perceive the missing frequencies. Such research makes it clear that distortions can be musical, this is indicated by a change from input to output that is perceived as the same sound through a harmonious relationship of the output frequencies.

Tan et al. (2003) *The Effect of Nonlinear Distortion on the Perceived Quality of Music and Speech Signals* – AES Journal, Volume 51, Issue 11.

The conclusion reached by Tan et al. through experiments documented in this paper was that 'an objective measure of nonlinear distortion based on the use of a multitone signal can predict the perceptual effects of nonlinear distortion reasonably well'. This means that provided we know the specific type of distortion an approximation of the subjective response can be made, if this is possible then perhaps we can find a reason that relatins to how music is perceived.

Hamm, R. (1973) *Tubes Versus Transistors-Is There an Audible Difference* – AES Journal, Volume 21, Issue 4.

This paper discusses the harmonic distortions and the subjective responses of tube/transistor designs when operated in their non-linear range; the range that is creatively abused by recording engineers to bring out a piece of equipment's 'musical qualities'. This paper shows the importance of harmonic relationships when dealing with our perception, interestingly the valve design emphasises the second harmonic while transistor designs suppress them; this provides potential clues to the musical
relationship of the corresponding distortions.

### Books

Miranda, E. (2002) - *Computer Sound Design; Synthesis & Programming Techniques* - 2nd Edition, Focal Press, UK.

Computer sound design is mainly focused on synthesis however much of this topic revolves around distorting sine waves with various filters as well as their effects on frequency. It contains a well written insight into understanding how these digital filters process sounds, their construction and their musical outcome.

Jourdain, R. (1997) *Music the Brain and Ecstasy* – 1st Edition, Harper Collins, US.

The over all theme of this book is an examination of why we derive so much pleasure from music. Jourdain tackles many interesting subjects in this book; particularly relevant are the chapters about how the hearing mechanisms and brain perceive sound in relation to or perceptive evolution. He also covers areas such as how the rules of music theory came about, how they relate to our perceptual hearing and how our subjective response is related to our cultural upbringing. Given that we are recording for people familiar with our cultures musical rules it seems likely our perception of distortions will parallel the same sensibilities.

Sacks, O. (2007) - *Musicophilia; Tales of Music & the Brain* - 1st Edition, Knopf, Canada.

This book contains a wealth of information relating music to our brains presented primarily through case studies. Sacks talks about different forms of Amusia; a condition where the brain does not to recognise various musical traits such as tone, harmony and rhythm. This is related to situations Sacks has encountered and to different patients neurological anomalies. Looking at our perception of music in this way can reinforce the idea that given certain rules such as music theory we can
determine a subjective response to a given distortion.

Horowitz & Hill (1994) *The Art of Electronics* - 2nd Edition, Cambridge University Press, US.

This book explains the foundations of electronics and the many results of electronic circuitry, it explains good and bad design along with the many pitfalls that are easy to miss. Many of the musical traits we associate with certain pieces of equipment are down to the design of the circuitry, an understanding of this permits an insight into the 'bare bones' of what happens to a waveform and why the distortions created might be musical.

Peretz & Zatorre (2003) - *The Cognitive Neuroscience of Music* - 1st Edition, Oxford University Press, US.

The main concern of this book is to understand the connection between our brains and music cognition/ability. Reretz and Zatorre, along with many contributors, present various findings in the field of cognitive neuroscience backed by experiment results specifically focused on music and its perception. I would hypothesise that the cognition of music is related to the perception of distortion and therefore this book is extremely relevant.

Roads, C. (1996) *The Computer Music Tutorial* – 1st Edition, MIT Press, UK.

This is a piece of technical core reading for those interested in digital signal processing. It provides an insight into how many forms of DSP are carried out and their effects on a signal. The chapter on digital filter design is extremely helpful in understanding their distortion effects, for instance comb filters exhibit peaks/nulls in a harmonic series (octaves). Knowing how these filters work is one of the first steps to understanding why certain designs are 'musical'.

Beament, J. (2005) - *How We Hear Music; The Relationship Between Music & The Hearing Mechanism* - 1st Edition, Boydell Press, UK.

How We Hear Music covers a lot of ground on the perception of music discussing various relationships between music and the brain. Of particular interest is the part about minimum duration needed for pitch to be perceived; with distortions that happen quickly like inter-sample clipping we may not be able to perceive their pitch and so will hear them as unmusical because no identifiable relationship can be formed.

### Articles

Kemp, M. (2003) *Sampling Equalisers* – Resolution, S2 Publications Ltd.

This article discusses the differences between analogue and digital equalisers. Here Kemp makes the case that current design is inadequate for creating complex filters, he also believes that the musical quality heard in various analogue filters is down to their complexity. Algorithmically this complexity is very difficult to recreate; instead Kemp suggests that analog designs can be dynamically sampled so that the input signals level determines the impulse response, this IR determines the coefficients used in a finite impulse response filter. Using this technique its possible to create an identical frequency/phase response between the analogue and digital equalisers. From here the filter coefficients derived from the IR can be modified (retaining the complexity) to fine tune the filter in order to be more 'musical'. 

### Interdisciplinary Source List

Barbati, S. (unknown) *A Perceptual Approach on Clipping and Saturation* – Simulanalog, [online: http://www.simulanalog.org/, accessed 07/12/10].

Geddes & Lee (2006) *Audibility of Linear Distortion with Variations in Sound Pressure Level and Group Delay* – AES eJournal, paper 6888.

Cabot, R. (1990) *Audible Effects vs. Objective Measurements in the Electrical Signal Path* - AES ejournal, paper 8-008.

Geddes & Lee (2003) *Auditory Perception of Nonlinear Distortion; Theory* – AES eJournal, paper 5890.

Geddes & Lee (2003) *Auditory Perception of Nonlinear Distortion* – AES eJournal, paper 5891.

Serafini, T. (unknown) *A Perceptual Approach to Equalisation* – Simulanalog, [online: http://www.simulanalog.org/, accessed 07/12/10].

Toulson, R. (2008) *Can We Fix It? – The consequences of ‘fixing it in the mix’ with common equalisation techniques are scientifically evaluated* – Art of Record Production eJournal, Issue 3. 

Irwin, M. (2009) *Distortion and Subjective Audio Quality* – Art of Record Production eJournal, not issued.

Yeh, D. (2009) *Digital Implementation of Musical Distortion Circuits By Analysis and Simulation* – Doctoral Dissertation for Stanford University.

Gan & Oo (2008) *Harmonic and Intermodulation Analysis of Nonlinear Devices Used in Virtual Bass Systems* – AES eJournal, paper 7403.

Hideo et al. (1980) *On the perception of Phase Distortion* – AES Journal, Volume 28, Issue 11.

Tzur & Colloms (1999) *The Effect of MaxxBass Psychoacoustic Bass Enhancement on Loudspeaker Design* – AES eJournal, paper 4892.

Tan et al. (2003) *The Effect of Nonlinear Distortion on the Perceived Quality of Music and Speech Signals* – AES Journal, Volume 51, Issue 11.

Hamm, R. (1973) *Tubes Versus Transistors-Is There an Audible Difference* – AES Journal, Volume 21, Issue 4.

Kemp, M. (2003) *Sampling Equalisers* – Resolution, S2 Publications Ltd.

Jourdain, R. (1997) *Music the Brain and Ecstasy* – 1st Edition, Harper Collins, US.

Sacks, O. (2007) - *Musicophilia; Tales of Music & the Brain* - 1st Edition, Knopf, Canada.

Peretz & Zatorre (2003) - *The Cognitive Neuroscience of Music* - 1st Edition, Oxford University Press, US.

Beament, J. (2005) - *How We Hear Music; The Relationship Between Music & The Hearing Mechanism* - 1st Edition, Boydell Press, UK.

### Further Reading (Pointers)
Moore, B (1997) *Psychology of Hearing* – Academic press, US. Referenced by Geddes in *Auditory perception of Nonlinear distortion*.

Leinonen & Curl (1977) *Method for Measuring Transient Intermodulation Distortion* (TIM) – AES Journal, Volume 25, Issue 4. Referenced by Barbati in *A Perceptual Approach to Clipping and Saturation*, controlling TIM is important in creating subjectively musical equipment.

Cabot et al. (1976) *Detection of Phase Shifts in Harmonically Related Material* – AES Journal, Volume 24, Issue 7. Referenced by Hideo et al. in *On the Perception of Phase Distortion*, a focus on harmonically related material is of particular interest.

Shpak, D. (1992) *Analytical design of Biquadratic Filter Sections For Parametric Filters* – AES Journal, Volume 40, Issue 11. Referenced by *Orfanidis in Digital Parametric Equaliser Design With Prescribed Nyquist-Frequency Gain*

---

# Research Notes

An interesting relationship between music and our brain is the order and structuring of what seems like chaos: Jourdain explains you cannot think of the brain like a computer, storing actions in specific places with a 'top to bottom command', instead it 'churns out information through a system of loops, and loops within loops, until centres concerned with every aspect of perception and movement are informed of what is going on and have had their say.'1 Similarly music relies on deep structure that is as well both 'everywhere and nowhere'; for instance the sound of a piano chord is a relationship between notes within it, each of these notes in turn have a timbal quality composed from a fundamental frequency and it harmonically related content. Observing this we see that the structure of even simple music can consist of overwhelmingly deep relationships; this can be paralleled in the functioning of our brains whereby even simple motion such a twitching a finger will cause thousands of neurones to fire, relaying interrelated messages to many parts of the brian.

This may not be seen as an original contribution to knowledge as many musicians, physicists and neurologists have made the same observation, however it is necessary to note this paralleling of 'order in chaos' occurs at nearly every stage when dealing with cognition; both music and the brain use overall form as an identifier rather than precise measurements.

Relating to the building of scales and the categorisation of harmonic discrepancies inherent in the Pythagorean method Jourdain states:

If scale tones are the building blocks of music, they had better be as square as possible if you want to build very high. That our tempered scale throws the Pythagorean tones slightly out of tune is unimportant because the tunings remain close enough to be categorised as Pythagorean, and it is to categorizations and not to precise tuning that we must attend.
