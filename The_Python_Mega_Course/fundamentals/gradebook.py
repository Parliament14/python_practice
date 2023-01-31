class gradebookFunctions:
    def findSum(gradebook: dict):
        return sum(gradebook.values())
    
    def findMean(gradebook: dict, sum: float):
        return sum / len(gradebook)
    
    def printGrades(gradebook):
        for student in gradebook.keys():
            print(f"Student {student} has the grade {gradebook[student]}")
    
gradebook = {"Jimmy":78, "Nathan": 95, "Maria":85 }
gradebookFunctions.printGrades(gradebook=gradebook)
mySum = gradebookFunctions.findSum(gradebook=gradebook)
print(f"Student grade sum: {mySum}")
mean = gradebookFunctions.findMean(gradebook=gradebook, sum=mySum)
print(f"Mean of the grades is: {mean}")