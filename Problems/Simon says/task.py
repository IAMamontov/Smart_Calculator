def what_to_do(instructions):
    phrase = "Simon says"
    if instructions.startswith(phrase):
        return "I" + instructions[len(phrase):]
    if instructions.endswith(phrase):
        return "I " + instructions[:len(phrase) + 1]
    return "I won't do it!"
