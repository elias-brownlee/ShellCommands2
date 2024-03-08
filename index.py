import random

class Process:
    #Initializes a process object with a given process ID and number of lottery tickets.
    def __init__(self, process_id, lottery_tickets):
        self.process_id = process_id
        self.lottery_tickets = lottery_tickets

class Scheduler:
    #Initializes a scheduler object to manage processes and perform lottery scheduling
    def __init__(self):
        self.processes = []  
        self.total_tickets = 0 
    #Adds a process to the scheduler and udates the total number of tickets
    def add_process(self, process):
        self.processes.append(process)
        self.total_tickets += process.lottery_tickets
    #Selects the next process to execute based on the lottery scheduling algorithm 
    def select_next_process(self):
        winning_ticket = random.randint(1, self.total_tickets)
        ticket_sum = 0

        for process in self.processes:
            ticket_sum += process.lottery_tickets
            if ticket_sum >= winning_ticket:
                #returns the selected process
                return process
        #if none are found then returns none
        return None  
#Just to demonstrate the lottery scheduling algorithm
def main():
    scheduler = Scheduler()
    processes_info = [(1, 10), (2, 30), (3, 20), (4, 40)]
    scheduler.processes = [Process(process_id, lottery_tickets) for process_id, lottery_tickets in processes_info]
    scheduler.total_tickets = sum(process.lottery_tickets for process in scheduler.processes)

    next_process = scheduler.select_next_process()
    if next_process:
        print("Selected Process ID:", next_process.process_id)
    else:
        print("No process selected.")

if __name__ == "__main__":
    main()