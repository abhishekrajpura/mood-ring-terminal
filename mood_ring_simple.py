#!/usr/bin/env python3
"""
Mood Ring Terminal - Interactive Version
A simplified version that works better across different platforms
"""

import time
import random
import os
import sys
from collections import deque

class SimpleMoodRing:
    def __init__(self):
        self.typing_speeds = deque(maxlen=10)
        self.current_mood = "neutral"
        self.mood_score = 50
        self.pattern_evolution = 0
        self.colors = {
            'excited': '\033[91m',     # Red
            'happy': '\033[93m',       # Yellow
            'calm': '\033[92m',        # Green
            'neutral': '\033[94m',     # Blue
            'thoughtful': '\033[95m',  # Magenta
            'mysterious': '\033[96m'   # Cyan
        }
        self.reset = '\033[0m'
        self.last_input_time = time.time()
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def calculate_mood_from_text(self, text, time_taken):
        """Calculate mood based on text length and time taken"""
        if not text.strip():
            return self.current_mood
            
        # Calculate approximate typing speed (chars per second)
        chars_per_second = len(text) / max(time_taken, 0.1)
        
        # Convert to approximate WPM (assuming 5 chars per word)
        wpm = (chars_per_second * 60) / 5
        self.typing_speeds.append(wpm)
        
        # Calculate average speed
        avg_speed = sum(self.typing_speeds) / len(self.typing_speeds)
        
        # Determine mood based on typing speed
        if avg_speed < 20:
            self.mood_score = max(10, self.mood_score - 5)
            return "thoughtful"
        elif avg_speed < 35:
            self.mood_score = min(70, max(30, self.mood_score + 2))
            return "calm"
        elif avg_speed < 50:
            self.mood_score = min(60, max(40, self.mood_score))
            return "neutral"
        elif avg_speed < 70:
            self.mood_score = min(80, self.mood_score + 3)
            return "happy"
        else:
            self.mood_score = min(100, self.mood_score + 5)
            return "excited"
    
    def generate_simple_pattern(self):
        """Generate a simpler pattern that works better in standard terminals"""
        patterns = {
            'excited': ['*', '!', '+', 'X', '#'],
            'happy': ['o', 'O', '@', '&', '%'],
            'calm': ['~', '-', '=', '.', '_'],
            'neutral': ['.', ':', ';', ',', '|'],
            'thoughtful': ['?', '/', '\\', '<', '>'],
            'mysterious': ['$', '#', '@', '&', '%']
        }
        
        mood_patterns = patterns.get(self.current_mood, patterns['neutral'])
        width = 50
        height = 8
        
        pattern_lines = []
        for y in range(height):
            line = ""
            for x in range(width):
                # Simpler pattern generation
                if random.random() < (self.mood_score / 200):
                    char = random.choice(mood_patterns)
                else:
                    char = ' '
                line += char
            pattern_lines.append(line)
        
        return pattern_lines
    
    def display_interface(self, user_text=""):
        self.clear_screen()
        color = self.colors.get(self.current_mood, self.colors['neutral'])
        
        # Header
        print(f"{color}{'=' * 52}{self.reset}")
        print(f"{color}        MOOD RING TERMINAL - INTERACTIVE{self.reset}")
        print(f"{color}{'=' * 52}{self.reset}")
        
        # Mood info
        print(f"\nMood: {color}{self.current_mood.upper()}{self.reset}")
        print(f"Score: [{'#' * (self.mood_score // 10)}{'.' * (10 - self.mood_score // 10)}] {self.mood_score}%")
        
        # Pattern
        pattern = self.generate_simple_pattern()
        print(f"\n{color}+{'-' * 50}+{self.reset}")
        for line in pattern:
            print(f"{color}|{line}|{self.reset}")
        print(f"{color}+{'-' * 50}+{self.reset}")
        
        # Instructions
        print("\nType something and press Enter to see your mood!")
        print("Type 'quit' to exit")
        
        # Show what user typed
        if user_text:
            print(f"\nYou typed: {user_text}")
            print(f"Speed: ~{int(sum(self.typing_speeds) / max(len(self.typing_speeds), 1))} WPM")
    
    def run(self):
        print("Welcome to Mood Ring Terminal!")
        print("Your typing speed will determine your digital mood.")
        print("\nPress Enter to start...")
        input()
        
        while True:
            self.display_interface()
            
            # Get user input with timing
            start_time = time.time()
            user_input = input("\n> ")
            end_time = time.time()
            
            if user_input.strip().lower() == 'quit':
                break
            
            # Calculate mood based on input
            time_taken = end_time - start_time
            self.current_mood = self.calculate_mood_from_text(user_input, time_taken)
            
            # Show result
            self.display_interface(user_input)
            time.sleep(2)  # Pause to show result
            
            # Add some mood drift
            self.mood_score = max(20, min(80, self.mood_score + random.randint(-2, 2)))
        
        # Exit message
        self.clear_screen()
        print(f"\n{self.colors['happy']}Thanks for using Mood Ring Terminal!{self.reset}")
        print(f"Your final mood: {self.colors[self.current_mood]}{self.current_mood}{self.reset}")
        print(f"Average typing speed: ~{int(sum(self.typing_speeds) / max(len(self.typing_speeds), 1))} WPM\n")

def main():
    # Enable ANSI colors on Windows
    if os.name == 'nt':
        os.system('color')
    
    mood_ring = SimpleMoodRing()
    
    try:
        mood_ring.run()
    except KeyboardInterrupt:
        print(f"\n\n{mood_ring.colors['happy']}Goodbye!{mood_ring.reset}")
    except Exception as e:
        print(f"\nError: {e}")
        print("Please make sure your terminal supports ANSI colors.")

if __name__ == "__main__":
    main()