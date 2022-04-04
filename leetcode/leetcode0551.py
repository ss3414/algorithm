# ****************************************************************分割线****************************************************************
# todo 0551（Student Attendance Record I）
# 学生出勤记录

class Solution:
    def checkRecord(self, s: str) -> bool:
        return not (s.count("A") > 1 or s.count("LLL") > 0)

# print(Solution().checkRecord("PPALLP"))
print(Solution().checkRecord("PPALLL"))
