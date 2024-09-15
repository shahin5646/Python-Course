# Add all value in a dictionary



marks   ={
    'python':75,
    'accounting':80,
    'system':85
}
total_marks=0
for numbers in marks.values():
    total_marks+=numbers
    
print(total_marks)