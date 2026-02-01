import sys
INF = 10**15

def solve():
    # Διαβάζουμε είσοδο
    n, B = map(int, sys.stdin.readline().split())
    S = sys.stdin.readline().strip()
    
    # Διάβασμα των κόστους αλλαγής
    cost = []
    for i in range(n):
        arr = list(map(int, sys.stdin.readline().split()))
        cost.append(arr)
    
    # dp[l][r] = dictionary {length: min_cost}
    # σημαίνει: μέσα στο διάστημα [l,r] ποιο είναι το ελάχιστο κόστος
    # για να φτιάξουμε παλινδρομική υποακολουθία συγκεκριμένου μήκους
    dp = [[dict() for _ in range(n)] for __ in range(n)]
    
    # Βάση: υποακολουθίες μήκους 1
    for i in range(n):
        # Αν κρατήσουμε μόνο το S[i], το κόστος είναι 0 (δεν χρειάζεται αλλαγή)
        dp[i][i][1] = 0
    
    # Εξετάζουμε διαστήματα με αυξανόμενο μήκος
    for length in range(2, n+1):
        for l in range(0, n-length+1):
            r = l + length - 1
            cur = dp[l][r]
            
            # 1. Παίρνουμε μόνο αριστερά ή δεξιά (δεν τα ταιριάζουμε)
            for k, cst in dp[l+1][r].items():
                if k not in cur or cur[k] > cst:
                    cur[k] = cst
            for k, cst in dp[l][r-1].items():
                if k not in cur or cur[k] > cst:
                    cur[k] = cst
            
            # 2. Αν προσπαθήσουμε να ταιριάξουμε το S[l] με το S[r]
            for c in range(26):
                # κόστος να κάνουμε και τα δύο άκρα το ίδιο γράμμα
                cost_lr = cost[l][c] + cost[r][c]
                
                if l+1 <= r-1:
                    # συνδυάζουμε με λύση μέσα στο [l+1,r-1]
                    for k, cst in dp[l+1][r-1].items():
                        new_len = k + 2
                        new_cost = cst + cost_lr
                        if new_len not in cur or cur[new_len] > new_cost:
                            cur[new_len] = new_cost
                else:
                    # μόνο τα δύο γράμματα (δεν έχει μέσα)
                    new_len = 2
                    new_cost = cost_lr
                    if new_len not in cur or cur[new_len] > new_cost:
                        cur[new_len] = new_cost
    
    # Τελική απάντηση: ψάχνουμε σε όλα τα μήκη της dp[0][n-1]
    ans = 0
    for k, cst in dp[0][n-1].items():
        if cst <= B:
            ans = max(ans, k)
    
    print(ans)


if __name__ == "__main__":
    solve()
