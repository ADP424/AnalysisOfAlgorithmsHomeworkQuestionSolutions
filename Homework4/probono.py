# searches until it finds the closest compatible job index
# log(n) running time
# def binary_search(jobs, curr_job):
#     high = len(jobs) - 1
#     low = 0

#     max_compatible_index = -1
#     while True:
#         mid = (high + low) // 2

#         if high < low:
#             return max_compatible_index
        
#         if jobs[mid][1] <= curr_job[0]:
#             max_compatible_index = mid
#             low = mid + 1
#         else:
#             high = mid - 1

# take in all the jobs as input
# takes O(n) time
num_jobs = int(input())
jobs = []
pro_bono_exists = False
for i in range(num_jobs):
    jobs.append([int(i) for i in input().split(' ')])
    if jobs[i][2] == 1:
        pro_bono_exists = True

if pro_bono_exists:
    jobs.sort(key = lambda job: job[1])

    I = [0 for _ in range(num_jobs)]

    last_compatible_index = 0
    for i in range(1, num_jobs):
        I[i] = max(1 + I[last_compatible_index], I[i - 1])
        # if the last added job's end date is less than the current job's start date, add the job
        if jobs[last_compatible_index][1] <= jobs[i][0]:
            last_compatible_index = i

    # ???????????????????????????????????????
    # S = [0 for _ in range(num_jobs)]

    # for i in range(num_jobs):
    #     if jobs[i][2] == 0: # is not pro bono
    #         S[i] = max(1 + S[binary_search(jobs, jobs[i])], S[i - 1])
    #     else:               # is pro bono
    #         S[i] = max(1 + I[binary_search(jobs, jobs[i])], S[i - 1])

    print(I[-1])
else:
    print(0)