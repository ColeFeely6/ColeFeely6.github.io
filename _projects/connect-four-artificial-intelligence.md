---
layout: page
title: Connect Four Artificial Intelligence 
description: A program that will optimally play variations of a Connect Four game against you using AI algorithms learned in CS 383
img: assets/img/connnect-four.jpeg
importance: 1
category: work
---

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/connnect-four.jpeg" title="connect four" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/ai.jpeg" title="ai" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
</div>


<a href="https://github.com/ColeFeely6/Connect-Four-Artificial-Intelligence">GitHub Repository</a>

Connect 4 Artificial Intelligence was a project in my Computer Science Artificial Intelligence class. This project was also a challenge, where every student's program was pinned against each other in a competition. The goal was to create an AI that would optimally play Connect-4 against you. 

Our programs had to be able to play on boards of varying dimensions, from anything like a 4x4 board, a 8x8 board, 6x7, 8x4, 12x8 and so on. 

The program first step was creating a baseline algorithm to find the next move. I used the Minimax Algorithm based on the utility. 

Next I used the heuristic evaluation as a baseline, where the heuristic evaluation is invoked when the Minimax algorithm reaches a certain depth limit. This evaluation is considered the "brain" of this Connect-4 bot. The function returns an estimated utility function (either positive or negative) for any game state. 

Finally, I implemented the Alpha-Beta Pruning algorithm, a more efficient and effective AI algorithm. 

The link to the repository is posted above, you can also check it out over on the repository tab on this website!

### Images Used

Connect-Four Image: https://m.media-amazon.com/images/I/81ZNRHJ+cIL.jpg

AI Image: https://imageio.forbes.com/specials-images/dam/imageserve/966248982/960x0.jpg?format=jpg&width=960


