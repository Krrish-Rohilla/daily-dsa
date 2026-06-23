class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int | None]:
        stack: list = []
        data = {}.fromkeys(range(n), 0)

        prev_log_id: int = 0
        prev_time: int = 0

        for log in logs:

            splited = log.split(":")
            start = True if splited[1]=="start" else False
            time: int = int(splited[2])
            log_id: int = int(splited[0])

            if not stack:
                stack.append([log_id,start,time])
                prev_time = time
                prev_log_id = log_id
                continue

            if start:
                data[prev_log_id] += time - prev_time - 1
                stack.append([log_id,start,time])
                prev_log_id = log_id

            else:
                data[prev_log_id] += time - prev_time + 1
                stack.pop()
                prev_log_id = stack[-1][0] if stack else 0

            prev_time = time

        return [data.get(x) for x in data]