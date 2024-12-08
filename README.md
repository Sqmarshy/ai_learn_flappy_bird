# 🐦 AI Learns Flappy Bird 🐦
This project demonstrates how to use the NEAT (NeuroEvolution of Augmenting Topologies) algorithm to train an AI agent to play the classic Flappy Bird game autonomously. By combining game mechanics, AI evolution, and neural networks, this repository provides a fully functional, self-learning Flappy Bird AI.

## 🌟 Features
- 🎮 Game Simulation: A Python implementation of the Flappy Bird game using pygame.
- 🧠 AI Training with NEAT: Utilizes the neat-python library to evolve neural networks for autonomous gameplay.
- 🎲 Dynamic Gameplay: Realistic mechanics including gravity, moving pipes, scrolling floor and pixel-wise collision detection.
- 🕹️ Manual and Autonomous Modes: Play manually or watch the AI learn and improve over generations.

## 🛠️ How it works
1. Game Mechanics: The bird must avoid pipes by flapping. The game includes features like gravity and collisions.
2. Collisions and Scoring: The AI learns to navigate pipes and optimize fitness.
3. NEAT Algorithm:  
    - Neural networks control the bird's actions.
     - Fitness is evaluated based on progress (e.g., surviving longer and passing pipes).
    - Over generations, the algorithm evolves better-performing networks.
  
## 📁 File Structure
- bird.py: Handles bird behavior, movement, and animations.
- pipe.py: Defines pipe obstacles, including random positioning and movement.
- floor.py: Simulates the scrolling floor.
- utils.py: Utility functions for rendering the game and detecting collisions.
- main.py: Core file for training the AI using NEAT.
- flappy_bird.py: A manual play version for testing or casual gameplay.
- config.py: Contains game configuration values like window dimensions.
- neat_config.txt: Configuration file for NEAT, including parameters like population size and mutation rates.

## ⚙️ NEAT Configuration
The neat_config.txt file defines the parameters for training the neural networks using NEAT. Key sections and their purposes include:
- 👥 Population and Fitness
    - pop_size: Number of networks per generation (default: 50).
    - fitness_criterion: The method for selecting the best networks (default: max).
    - fitness_threshold: The fitness score required to stop training (default: 1000).
- 🔄 MutationRates
    - conn_add_prob: Probability of adding a connection between nodes (default: 0.5).
    - conn_delete_prob: Probability of removing a connection (default: 0.5).
    - node_add_prob: Probability of adding a new node (default: 0.2).
    - node_delete_prob: Probability of deleting an existing node (default: 0.2).
- ⚡ Activation Functions
    - activation_default: The default activation function for nodes (default: tanh).
    - activation_options: Available activation functions (default: tanh).
- 🏗️ Network Structures
    - feed_forward: Specifies whether networks are feed-forward only (default: True).
    - num_inputs: Number of input neurons (default: 3, representing bird position and pipe distances).
    - num_outputs: Number of output neurons (default: 1, controlling whether the bird flaps).
- 🎯 Fitness Evaluation
    - Fitness increases when the bird passes a pipe.
    - Fitness decreases when the bird hits a pipe or goes out of bounds.
This configuration ensures that networks evolve efficiently, balancing exploration and exploitation while minimizing overfitting.

## 🖥️ Requirements
- Python 3.x
- Libraries:
    - pygame
    - neat-python

## 🚀 Setup
- Clone the repo and install required libraries:  
    ```bash
    git clone https://github.com/Sqmarshy/ai_learn_flappy_bird.git
    cd ai_learn_flappy_bird
    pip install pygame neat-python
    ```
## 🎮 Usage
Run main.py for the AI version and flappy_bird.py for a manual game~

## 🌟 Future Enhancements
- Add real-time visualizations of the neural network decision-making process.
- Implement a leaderboard to track and compare AI generations' performance.
- Enhance graphics and animations for improved gameplay experience.
