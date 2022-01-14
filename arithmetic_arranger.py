def arithmetic_arranger(problems, answer = False):
    
    fail = 0
    if len(problems) > 5:
        fail = 1        
    
    count = 0
    
    nums_aligned_top = '' 
    nums_aligned_bottom = '' 
    traces = '' 
    answers = '' 
    
    for problem in problems:
        nums = []
        conta = problem.split()
        nums.append(conta[0])
        nums.append(conta[2])
        
        if conta[1] not in ['+', '-']:
            fail = 2
            break
        
        if conta[0].isdigit() == False or conta[2].isdigit() == False:
            fail = 3
            break
        
        if len(conta[0]) > 4 or len(conta[2]) > 4:
            fail = 4
            break

        max_len = 0        
        diff = len(nums[0]) - len(nums[1])

        if len(nums[0]) >= len(nums[1]):
            max_len = len(nums[0])
        else:
            max_len = len(nums[1])
       
        trace = ''
        for i in range(max_len + 2):
            trace = trace + '-'
            
        if count == 0:
            traces = traces + trace
        else:
            traces = traces + ' '*4 + trace
            
        if answer == True:
            if conta[1] == '+':
                ans = int(nums[0]) + int(nums[1])
            else:
                ans = int(nums[0]) - int(nums[1])
                
            if count == 0:
                answers = answers + ' '*(len(trace) - len(str(ans))) + str(ans)
            else:
                answers = answers + ' '*4 + ' '*(len(trace) - len(str(ans))) + str(ans)
            
        if diff > 0:
            nums[1] = conta[1] + ' '*(1 + diff) + nums[1]
            if count == 0:
                nums_aligned_top = nums_aligned_top + ' '*2 + nums[0]
                nums_aligned_bottom = nums_aligned_bottom + nums[1]
            else:
                nums_aligned_top = nums_aligned_top + ' '*4 + ' '*2 + nums[0]
                nums_aligned_bottom = nums_aligned_bottom + ' '*4 + nums[1]
            
        else:
            nums[1] = conta[1] + ' ' + nums[1]
            if count == 0:
                nums_aligned_top = nums_aligned_top + ' '*(2 + abs(diff)) + nums[0]
                nums_aligned_bottom = nums_aligned_bottom + nums[1]
            else:
                nums_aligned_top = nums_aligned_top + ' '*4 + ' '*(2 + abs(diff)) + nums[0]
                nums_aligned_bottom = nums_aligned_bottom + ' '*4 + nums[1]
        
        count += 1
    
    if fail == 1:
        return 'Error: Too many problems.'
    elif fail == 2:
        return "Error: Operator must be '+' or '-'."
    elif fail == 3:
        return 'Error: Numbers must only contain digits.'
    elif fail == 4:
        return 'Error: Numbers cannot be more than four digits.'
    else:
        if answer == True:
            arranged_problems = nums_aligned_top + '\n' + nums_aligned_bottom + '\n' + traces + '\n' + answers
        else:
            arranged_problems = nums_aligned_top + '\n' + nums_aligned_bottom + '\n' + traces
        
        return arranged_problems
