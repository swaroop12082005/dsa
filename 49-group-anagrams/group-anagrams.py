class Solution(object):
    def groupAnagrams(self, strs):

        # Create an empty dictionary
        groups = {}

        # Go through each word in the list
        for word in strs:

            # Sort the word and make it a string
            key = "".join(sorted(word))

            # If the key is not in the dictionary,
            # create an empty list for it
            if key not in groups:
                groups[key] = []

            # Add the current word to its group
            groups[key].append(word)

        # Return all the groups
        return list(groups.values())