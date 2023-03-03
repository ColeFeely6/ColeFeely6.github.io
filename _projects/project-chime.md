---
layout: page
title: Project Chime 
description: An Audio Data Transfer System Over Commodity Embedded Devices
img: assets/img/wave2.png
importance: 3
category: work
---

## IMPORTANT LINKS

<a href="https://github.com/ColeFeely6/Project-Chime">GitHub Repository</a>

<a href="https://github.com/ColeFeely6/Project-Chime/blob/main/ECE%20597-SD-Final-Report.pdf">Full Report</a>


## Project Context

Members: Cole Feely, Aidan Murray, Owen Lheron and Sashank Rao

Start Date: Sept. 27, 2022

Due Date: December 8, 2022

## Poster

<div class="container">
    <div class="row">
        <div class="col-sm mt-3 mt-md-0">
            {% include figure.html path="assets/img/chime-poster.jpeg" title="poster" class="img-fluid rounded z-depth-1" %}
        </div>
    </div>
    <div class="caption">
        Our Poster for the Project
    </div>
</div>

## Background 

There are some communication methods of data transfer using sensing signals with low-cost sensors but these systems produce low sampling rates which are not as efficient than high cost solutions with high sampling rates. We will investigate how we can improve sensing signal data transfer with low-cost sensors with low sampling rates by minimizing the error and noise rates commonly encountered.

## Goal

Encode data into an audio sensing signal and send it to a receiver where decoding algorithms will be performed to interpret the data.

## Deliverables

Demonstrate our goal with a modulation that best circumvents noise from audio channels, human speech or other background interference. Demonstrate better a reduction in the error rate from these interferences than off the shelf solutions Minimize decoding errors in the absence of symbol frame synchronization between the sender and receiver

## Hardware

Receiver/ Sender: Arduino Uno Speaker: Personal Computer Speaker or a Piezo Buzzer Microphone: SparkFun Electret Microphone Breakout Other: Power Supply, Capacitors, Resistors, Jumpers etc.

## Team Roles

Logistics: Cole Feely
SBC: Cole Feely
Hardware Filter: Aidan Murray
FFT: Owen Lheron
Signal Deconstruction: Sash Rao


## Block Diagram 

<div class="container">
    <div class="row">
        <div class="col-sm mt-3 mt-md-0">
            {% include figure.html path="assets/img/chime-block-diagram.jpeg" title="chime block diagram" class="img-fluid rounded z-depth-1" %}
        </div>
    </div>
</div>

## Results

Check out our results in our Final Academic Paper:

<a href="https://github.com/ColeFeely6/Project-Chime/blob/main/ECE%20597-SD-Final-Report.pdf">Full Report</a>
