class processes:
    def __init__(self, id, at, bt, ct):
        self.id = id
        self.at = at
        self.bt = bt
        self.ct = ct
        self.tat = self.ct-self.at
        self.wt = self.tat-self.bt

    def get(self):
        print(f"{self.id}\t{self.at}\t{self.bt}\t{self.ct}\t{self.tat}\t{self.wt}")

    def turnaround(self):
        return self.tat

    def waiting(self):
        return self.wt


num = int(input("Enter the Number of Processes:"))
l = []
ct = 0

for i in range(num):

    print(f'Process {i+1}')
    at = int(input("Enter the Arrival Time:-"))
    bt = int(input("Enter the Burst Time:-"))
    if (len(l) == 0):
        ct = bt
        l.append(processes(i, at, bt, ct))
    else:
        ct += bt
        l.append(processes(i, at, bt, ct))

    print("\n")
avg_tat = 0
avg_wat = 0
print("PID\tAT\tBT\tCT\tTAT\tWT")
for process in l:
    process.get()

for process in l:
    avg_tat += process.turnaround()
    avg_wat += process.waiting()
print(f"Avg_turnaround:{avg_tat/num}\nAvg_Waitingtime:{avg_wat/num}")