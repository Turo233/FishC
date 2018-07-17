class List():
        def __init__(self, *args):
                self.keys = [x for x in args]
                self.count = {}.fromkeys(self.keys, 0)

        def counter(self, index):
                return self.count[self.keys[index]]
        
        def __len__(self):
                return len(self)
        
        def __getitem__(self, key):
                self.count[self.keys[key]] += 1
                return self.keys[key]
        
        def __setitem__(self, key, value):
                self.keys[key] = value
                
        def __delitem__(self, key):
                del self.count[self.keys[key]]
                del self.keys[key]
                
        def append(self, key):
                self.keys.append(key)
                self.count[key] = 0

        def pop(self):
                print(self.keys[-1])
                del self.count[self.keys[-1]]
                del self.keys[-1]
                
        def remove(self, key):
                del self.count[key]
                self.keys.remove(key)
                
        def insert(self, index, key):
                self.keys.insert(index, key)
                self.count[key] = 0
                
        def clear(self):
                self.keys.clear()
                self.count.clear()
        def reverse(self):
                self.keys.reverse()
