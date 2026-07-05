class HashMap:

    def __init__(self, initial_capacity=10):
        self.buckets = []
        for _ in range(initial_capacity):
            self.buckets.append([])

    def insert(self, key, item):
        bucket = hash(key) % len(self.buckets)
        bucket_list = self.buckets[bucket]

        for key_value in bucket_list:
            if key_value[0] == key:
                key_value[1] = item
                return True

        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    def lookup(self, key):
        bucket = hash(key) % len(self.buckets)
        bucket_list = self.buckets[bucket]

        for key_value in bucket_list:
            if key_value[0] == key:
                return key_value[1]

        return None
