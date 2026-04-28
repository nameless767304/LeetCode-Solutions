class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        tracker = k
        time = 0

        while tickets and not (tracker == 0 and tickets[tracker] == 1):
            time += 1
            ticket = tickets.pop(0)
            if ticket != 1:
                tickets.append(ticket - 1)
            
            if tracker == 0:
                tracker = len(tickets) - 1
            else:
                tracker -= 1

        return time + 1
                
