# Lyra Word Generator
# P–A–E construction model

def generate_word(P, A, E):
    return P + A + E

def explain_word(word_dict):
    return f"{word_dict['P']}-{word_dict['A']}-{word_dict['E']}: {word_dict['meaning']}"

if __name__ == "__main__":
    from pathlib import Path
    import json

    lexicon = json.loads(Path("data/lexicon.json").read_text(encoding="utf-8"))
    for word, info in lexicon.items():
        print(f"{word}: {explain_word(info)}")
