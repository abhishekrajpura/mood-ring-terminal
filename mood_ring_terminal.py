#!/usr/bin/env python3
"""
Mood Ring Terminal - An interactive ASCII art generator that responds to your typing speed
and creates evolving patterns based on your "digital mood"
"""

import time
import random
import os
import sys
import threading
from collections import deque
from datetime import datetime

class MoodRingTerminal:
    def __init__(self):
        self.typing_speeds = deque(maxlen=10)
        self.current_mood = "neutral"
        self.mood_score = 50
        self.pattern_evolution = 0
        self.colors = {
            'excited': '\033[91m',  # Red
            'happy': '\033[93m',    # Yellow
            'calm': '\033[92m',     # Green
            'neutral': '\033[94m',  # Blue
            'thoughtful': '\033[95m', # Magenta
            'mysterious': '\033[96m'  # Cyan
        }
        self.reset = '\033[0m'
        self.running = True
        self.user_input = ""
        self.last_keypress = time.time()
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def calculate_mood(self):
        if not self.typing_speeds:
            return "neutral"
        
        avg_speed = sum(self.typing_speeds) / len(self.typing_speeds)
        
        # Mood based on typing speed (words per minute approximation)
        if avg_speed < 20:
            self.mood_score = max(0, self.mood_score - 2)
            return "thoughtful"
        elif avg_speed < 40:
            self.mood_score = min(100, max(30, self.mood_score + 1))
            return "calm"
        elif avg_speed < 60:
            self.mood_score = min(100, max(40, self.mood_score))
            return "neutral"
        elif avg_speed < 80:
            self.mood_score = min(100, self.mood_score + 2)
            return "happy"
        else:
            self.mood_score = min(100, self.mood_score + 3)
            return "excited"
    
    def generate_pattern(self):
        patterns = {
            'excited': ['*', '!', '^', '◆', '★', '✦'],
            'happy': ['♪', '♫', '◕', '◔', '◐', '◑'],
            'calm': ['~', '≈', '∞', '○', '◯', '⊙'],
            'neutral': ['·', '•', '◦', '▪', '▫', '□'],
            'thoughtful': ['?', '¿', '∴', '∵', '∷', '∶'],
            'mysterious': ['§', '¤', '※', '⊕', '⊗', '⊜']
        }
        
        mood_patterns = patterns.get(self.current_mood, patterns['neutral'])
        width = 60
        height = 10
        
        # Create evolving pattern based on mood score and time
        pattern_lines = []
        for y in range(height):
            line = ""
            for x in range(width):
                # Complex pattern generation based on mood score and evolution
                wave = int(5 * abs(self.mood_score/20 * 
                          (1 + 0.5 * random.random()) * 
                          (1 + 0.3 * (x/width)) * 
                          (1 + 0.2 * (y/height))))
                
                if (x + self.pattern_evolution) % wave == 0:
                    char = random.choice(mood_patterns)
                else:
                    char = ' '
                line += char
            pattern_lines.append(line)
        
        return pattern_lines
    
    def display_interface(self):
        self.clear_screen()
        color = self.colors.get(self.current_mood, self.colors['neutral'])
        
        print(f"{color}╔{'═' * 60}╗")
        print(f"║{'MOOD RING TERMINAL'.center(60)}║")
        print(f"║{'Type to see your digital mood evolve!'.center(60)}║")
        print(f"╚{'═' * 60}╝{self.reset}")
        
        print(f"\nCurrent Mood: {color}{self.current_mood.upper()}{self.reset}")
        print(f"Mood Score: {'█' * (self.mood_score // 5)}{'░' * (20 - self.mood_score // 5)} {self.mood_score}%")
        
        # Display the pattern
        pattern = self.generate_pattern()
        print(f"\n{color}┌{'─' * 60}┐{self.reset}")
        for line in pattern:
            print(f"{color}│{line}│{self.reset}")
        print(f"{color}└{'─' * 60}┘{self.reset}")
        
        # Display typing area
        print(f"\n{color}Type your thoughts (or 'quit' to exit):{self.reset}")
        print(f"> {self.user_input}", end='', flush=True)
    
    def update_display(self):
        while self.running:
            self.pattern_evolution += 1
            self.current_mood = self.calculate_mood()
            
            # Add some mood drift over time
            if time.time() - self.last_keypress > 3:
                self.mood_score = max(20, min(80, self.mood_score + random.randint(-2, 2)))
            
            self.display_interface()
            time.sleep(0.5)
    
    def run(self):
        display_thread = threading.Thread(target=self.update_display)
        display_thread.daemon = True
        display_thread.start()
        
        print("Welcome to Mood Ring Terminal!")
        print("Start typing to see your digital mood manifest...")
        time.sleep(2)
        
        word_start_time = time.time()
        char_count = 0
        
        try:
            while self.running:
                char = sys.stdin.read(1)
                
                if char == '\n':
                    if self.user_input.strip().lower() == 'quit':
                        self.running = False
                        break
                    
                    # Calculate typing speed for the line
                    time_elapsed = time.time() - word_start_time
                    if time_elapsed > 0 and char_count > 0:
                        # Approximate WPM (assuming 5 chars per word)
                        wpm = (char_count / 5) / (time_elapsed / 60)
                        self.typing_speeds.append(wpm)
                    
                    self.user_input = ""
                    char_count = 0
                    word_start_time = time.time()
                else:
                    self.user_input += char
                    char_count += 1
                    self.last_keypress = time.time()
                    
                    # Update typing speed periodically
                    if char == ' ':
                        time_elapsed = time.time() - word_start_time
                        if time_elapsed > 0.1:
                            wpm = (char_count / 5) / (time_elapsed / 60)
                            self.typing_speeds.append(wpm)
                            word_start_time = time.time()
                            char_count = 0
                
        except KeyboardInterrupt:
            self.running = False
        
        self.clear_screen()
        print(f"\n{self.colors['happy']}Thanks for sharing your digital mood!{self.reset}")
        print(f"Your final mood was: {self.colors[self.current_mood]}{self.current_mood}{self.reset}")
        print(f"Average mood score: {self.mood_score}%\n")

def main():
    # Check if terminal supports ANSI colors
    if os.name == 'nt':
        os.system('color')
    
    mood_ring = MoodRingTerminal()
    
    # Set terminal to raw mode for character-by-character input
    if os.name != 'nt':
        import termios, tty
        old_settings = termios.tcgetattr(sys.stdin)
        try:
            tty.setraw(sys.stdin.fileno())
            mood_ring.run()
        finally:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
    else:
        # Windows doesn't support raw mode the same way
        print("Note: On Windows, press Enter after each line for best experience")
        mood_ring.run()

if __name__ == "__main__":
    main()