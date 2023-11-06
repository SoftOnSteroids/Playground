def knapsack(capacity_knap:int, items_weight:list, items_value:list, i:int):
    # Return 0 if knapsack is full or are no more items to put into
    if i < 0 or capacity_knap == 0:
        return 0
    
    # Try next if item is heaviest than knapsack capacity
    if items_weight[i] > capacity_knap:
        return knapsack(capacity_knap, items_weight, items_value, i-1)
    
    # Look for highest load value with and withput item
    return max(items_value[i] + knapsack(capacity_knap - items_weight[i], items_weight, items_value, i-1),
               knapsack(capacity_knap, items_weight, items_value, i-1))

if __name__ == "__main__":
    capacity_knap = 15
    items_value = [3,2,2,8,4]
    items_weight = [10,8,4,4,12]

    print(knapsack(capacity_knap, items_weight, items_value, len(items_value)-1))