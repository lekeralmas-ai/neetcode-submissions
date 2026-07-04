class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = list()
        for email in emails:
            local, domain = email.split('@')
            corrected_email = ""
            for i in range(len(local)):
                if local[i] == '+':
                    break
                if local[i] != '.':
                    corrected_email += local[i]
            corrected_email += '@' + domain
            if corrected_email not in res:
                res.append(corrected_email)
        return len(res)
