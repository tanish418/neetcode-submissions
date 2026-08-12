class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()

        for email in emails:
            name, domain = email.split("@")
            name = name.replace(".", "")
            name = name.split("+")[0]

            unique.add(name + "@" + domain)

        return len(unique)