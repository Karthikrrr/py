with open("boss.txt") as f:
    lines = f.readlines()
    lines = [l for l in lines if "ROW" in l]
    with open("boss1.txt", "w") as f1:
        f1.writelines(lines)
