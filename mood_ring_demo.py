#!/usr/bin/env python3
"""
Mood Ring Terminal Demo - Shows the visual effects without real-time input
"""

import time
import random
import os
import sys

class MoodRingDemo:
    def __init__(self):
        self.moods = ['thoughtful', 'calm', 'neutral', 'happy', 'excited', 'mysterious']
        self.current_mood_index = 2  # Start with neutral
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
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def generate_pattern(self, mood):
        patterns = {
            'excited': ['*', '!', '^', '◆', '★', '✦'],
            'happy': ['♪', '♫', '◕', '◔', '◐', '◑'],
            'calm': ['~', '≈', '∞', '○', '◯', '⊙'],
            'neutral': ['·', '•', '◦', '▪', '▫', '□'],
            'thoughtful': ['?', '¿', '∴', '∵', '∷', '∶'],
            'mysterious': ['§', '¤', '※', '⊕', '⊗', '⊜']
        }
        
        mood_patterns = patterns.get(mood, patterns['neutral'])
        width = 60
        height = 10
        
        # Create evolving pattern
        pattern_lines = []
        for y in range(height):
            line = ""
            for x in range(width):
                # Pattern generation based on mood score and evolution
                wave = int(5 * abs(self.mood_score/20 * 
                          (1 + 0.5 * random.random()) * 
                          (1 + 0.3 * (x/width)) * 
                          (1 + 0.2 * (y/height))))
                
                if wave > 0 and (x + self.pattern_evolution) % wave == 0:
                    char = random.choice(mood_patterns)
                else:
                    char = ' '
                line += char
            pattern_lines.append(line)
        
        return pattern_lines
    
    def display_frame(self, mood):
        self.clear_screen()
        color = self.colors.get(mood, self.colors['neutral'])
        
        # Header
        print(f"{color}╔{'═' * 60}╗")
        print(f"║{'MOOD RING TERMINAL - DEMO MODE'.center(60)}║")
        print(f"║{'Watch the moods cycle automatically!'.center(60)}║")
        print(f"╚{'═' * 60}╝{self.reset}")
        
        # Mood info
        print(f"\nCurrent Mood: {color}{mood.upper()}{self.reset}")
        print(f"Mood Score: {'█' * (self.mood_score // 5)}{'░' * (20 - self.mood_score // 5)} {self.mood_score}%")
        
        # Pattern display
        pattern = self.generate_pattern(mood)
        print(f"\n{color}┌{'─' * 60}┐{self.reset}")
        for line in pattern:
            print(f"{color}│{line}│{self.reset}")
        print(f"{color}└{'─' * 60}┘{self.reset}")
        
        # Instructions
        print(f"\n{color}Press Ctrl+C to exit the demo{self.reset}")
    
    def run_demo(self):
        print("Starting Mood Ring Terminal Demo...")
        print("The mood will automatically cycle through different states.")
        print("Press Ctrl+C to exit.\n")
        time.sleep(3)
        
        try:
            while True:
                # Cycle through moods
                current_mood = self.moods[self.current_mood_index]
                
                # Update mood score based on current mood
                if current_mood == 'excited':
                    self.mood_score = min(100, self.mood_score + 3)
                elif current_mood == 'happy':
                    self.mood_score = min(90, self.mood_score + 2)
                elif current_mood == 'calm':
                    self.mood_score = max(30, min(70, self.mood_score + random.randint(-1, 1)))
                elif current_mood == 'neutral':
                    self.mood_score = max(40, min(60, self.mood_score + random.randint(-1, 1)))
                elif current_mood == 'thoughtful':
                    self.mood_score = max(10, self.mood_score - 2)
                elif current_mood == 'mysterious':
                    self.mood_score = random.randint(20, 80)
                
                # Display current frame
                self.display_frame(current_mood)
                
                # Evolve pattern
                self.pattern_evolution += 1
                
                # Stay in each mood for a few seconds
                time.sleep(0.5)
                
                # Change mood every ~5 seconds (10 frames)
                if self.pattern_evolution % 10 == 0:
                    self.current_mood_index = (self.current_mood_index + 1) % len(self.moods)
                
        except KeyboardInterrupt:
            self.clear_screen()
            print(f"\n{self.colors['happy']}Thanks for watching the Mood Ring Terminal demo!{self.reset}")
            print(f"The full version responds to your typing speed in real-time.\n")

def main():
    # Enable ANSI colors on Windows
    if os.name == 'nt':
        os.system('color')
    
    demo = MoodRingDemo()
    demo.run_demo()

if __name__ == "__main__":
    main()