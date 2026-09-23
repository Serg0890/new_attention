class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.__cache = {}
        self.order = []

    @property
    def cache(self):
        key_for_del = self.order[0]
        result = key_for_del, self.__cache[key_for_del]
        return result

    @cache.setter
    def cache(self, new_elem):
        key, value = new_elem
        if key in self.__cache:
            # Перемещаем ключ в конец списка order
            self.order.remove(key)
            self.order.append(key)
        else:
            # Добавляем новый ключ в кэш и список order
            self.__cache[key] = value
            self.order.append(key)

            # Если превышен лимит capacity, удаляем самый старый элемент
            if len(self.order) > self.capacity:
                oldest_key, oldest_value = self.cache
                self.order.pop(0)
                del self.__cache[oldest_key]

    def get(self, key):
        if key in self.__cache:
            # Перемещаем ключ в конец списка order
            self.order.remove(key)
            self.order.append(key)
            return self.__cache[key]
        else:
            return None

    def print_cache(self):
        print("LRU Cache:")
        for key in self.order:
            print(key, ":", self.__cache[key])