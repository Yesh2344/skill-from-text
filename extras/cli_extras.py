import argparse

def main:
 parser = argparse.ArgumentParser
 parser.add_argument('--text', help='Text to convert to a skill')
 args = parser.parse_args
 print(f'Converting {args.text} to a skill')