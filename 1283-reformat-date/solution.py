class Solution:
    def reformatDate(self, date: str) -> str:
        months = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
        day, month, year = date.split()
        day = "0" + str(day[0]) if len(day) == 3 else str(day[0:2])
        month = months[month]

        return f"{year}-{month}-{day}"
        
