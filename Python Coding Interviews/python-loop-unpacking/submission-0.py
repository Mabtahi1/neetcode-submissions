from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    max = 0
    max_score = []
    for student, score in scores:
        if score > max:
            max_score = student
            max = score
    return max_score        


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
