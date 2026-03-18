def unlocked_layers(answers):
    print("DEBUG ANSWERS:", answers)
    layers = ["layer1"]

    if all(answers.get(x) for x in["problem","audience","alternative"]):
        print("UNLOCKING LAYER 2")
        layers.append("layer2")

    return layers