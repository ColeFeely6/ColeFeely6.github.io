---
layout: page
title: Junior Design Project
description: A Social Distancing Monitoring System
img: assets/img/jdp1.jpeg
importance: 1
category: work
---

## Social Distancing Monitoring System: Junior Design Project

- Date Completed: May 9, 2022


- Course Number: ECE 304

<div class="container">
    <div class="row">
        <div class="col-sm mt-3 mt-md-0">
            {% include figure.html path="assets/img/jdp1.jpeg" title="jdp1" class="img-fluid rounded z-depth-1" %}
        </div>
    </div>
</div>

### Important Links

<a href="https://youtu.be/32ZztrYxNW0">YouTube Demonstration</a>
<a href="https://github.com/ColeFeely6/Junior-Design-Project">GitHub</a>

## Introduction

This report will serve as an overview of the final build’s tests and results. This build was
expected to meet the specifications laid out in the second preliminary design review. As expected
in any engineering project, the results were not exactly as predicted before the build was
initiated. Overall, this build serves to lay the groundwork for the main functionalities of the
device. Section 1 will go over the previous plans and tests, Section 2 will denote design changes
and Section 3 will design the results of the tests.

## Problem Statement

Limiting exposure and spread of the COVID-19 virus is vital for protecting our communities and
by following safety protocols issued by public health agencies, we can reduce the number of
fatalities and time spent under COVID restrictions. One of these safety protocols issued by
public health agencies is that individuals should maintain six feet apart from one another. This
can be challenging for those that work at front desks or are in contact with many people at the
office throughout the day. To ensure the safety of everyone, the Covid-19 Distance Sensor (CDS)
detects the distance of those approaching the front desk and alerts them if they break compliance
by displaying the distance of the individual and flashing a red light if they are within 6 feet. If
compliance is not broken, then the device will display a green light, signifying that it is safe to
either approach or being a conversation with the person at the front desk. Additionally for the
user, the CDS will track the number of individuals that approach the desk according to a ti-e
period and the minimum distance of the most recent visitors. 

## Design Requirements

1. Automatically detect patrons that are up to 10 feet away
2. Shall track the distance of the approaching individual and display it for the visitor and the
user
3. Will alert both the approaching individual that they are in violation with an LED
4. The system will utilize a display for the approaching party to show their distance from
the desk
5. The system will employ another display for the desk attendant that details the distance of
the current patron
6. The desk attendant display will also show the minimum two distances of the patrons
7. The build must be powered by a 9V Battery


<div class="container">
    <div class="row">
        <div class="col-sm mt-3 mt-md-0">
            {% include figure.html path="assets/img/jdp3.jpeg" title="jdp3" class="img-fluid rounded z-depth-1" %}
        </div>
    </div>
</div>


## Design Changes

I added multiple minimum distances rather than just two because I thought this would be more
insightful for the operator. This was a positive design change rather than removing.

## Test Results and Conclusion 

This build was able to reach all design requirements fully specified in the preliminary design
review of the devices provided. The seven-segment display was buggy in that it flashed each
time it was updated which made it hard to read and look unprofessional. The sonar also did not
have the capabilities that I thought previously. Other than that, all requirements were met and
displayed in the video demonstration.
Overall, this project required a lot of time and dedication. It was very difficult but because I ran
into so many bugs, I feel like I understand every step and component of this build. I knew every
pin on the chip, every wire on the board and every line of code in this build. I may have been
frustrated doing it but after completing the project, I felt accomplished, and I feel confident with
these skills going into Senior Design Project. 