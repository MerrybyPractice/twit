from collections import deque
class Utilities: 
    def __init__(self): 
        self.read_dict = {}
    
    
    def read_in_resources(self, res_file): 
        """Reads in resources/res_file.txt and makes the contents avaliable to twit

        :param res_file: The path to the required res_file (search_req.txt, twt_secrets.txt, ect)
        :type res_file: string
        """
        with open(res_file, "r") as rf:
            contents = rf.readlines()

        for ln in range(len(contents)): 
            line = contents[ln].split("=")
            self.read_dict[line[0]] = line[1].strip()

class Search: 
    def __init__(self, search_req_dict):
        self.query_string=search_req_dict.get("query_string")
        self.geocode=search_req_dict.get("geocode") or None 
        self.lang=search_req_dict.get("lang") or None
        self.locale=search_req_dict.get("local") or None
        self.result_type=search_req_dict.get("result_type") or 'recent' 
        self.count=search_req_dict.get("count") or 100
        self.until=search_req_dict.get("until") or None
        self.since_id=search_req_dict.get("since_id") or None 
        self.max_id=search_req_dict.get("max_id") or None 
        self.include_entities=search_req_dict.get("include_entities") or True 
        self.enviornment_name_query=search_req_dict.get("enviornment_name") or None
        self.tag=search_req_dict.get("tag") or None
        self.fromDate=search_req_dict.get("fromDate") or None
        self.toDate=search_req_dict.get("toDate") or None
        self.maxResults=search_req_dict.get("maxResults") or None
        self.next=search_req_dict.get("next") or None
        #search deque
        self.search_results = deque()
        
            
