cached = {}

class GuildsPrefixes:
    def __init__(self, cache_dict):
        self.prefixes = cache_dict
    def add(self, guild_id, new_prefix):
        self.prefixes[guild_id] = new_prefix
    def get(self, guild_id):
        return self.prefixes.get("$")
