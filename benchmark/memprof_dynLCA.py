Filename: /home/giuseppec/miniconda3/envs/bw2/lib/python3.6/site-packages/bw2temporalis/dynamic_lca.py

Line #    Mem usage    Increment   Line Contents
================================================
    83    164.5 MiB    164.5 MiB       def calculate(self):
    84                                     """Calculate"""
    85    164.5 MiB      0.0 MiB           self.timeline = Timeline()
    86    164.5 MiB      0.0 MiB           self.heap = [] #heap with dynamic exchanges to loop over (impact,edge,datetime, TemporalDistribution)
    87    164.5 MiB      0.0 MiB           self.calc_number = 0
    88                                     
    89                                     #run worst case LCA if lca_object not passed else redo for demand and worst_case method
    90    164.5 MiB      0.0 MiB           if self.lca_object:
    91                                         _redo_lcia(self, self.lca_object, self.demand,self.worst_case_method)
    92                                     else:
    93    164.5 MiB      0.0 MiB               self.lca = LCA(self.demand,self.worst_case_method)
    94    261.5 MiB     97.0 MiB               self.lca.lci()
    95    261.6 MiB      0.2 MiB               self.lca.lcia()
    96                                     
    97                                     #reverse matrix and calculate cutoff
    98    262.6 MiB      1.0 MiB           self.reverse_activity_dict, self.reverse_prod_dict, self.reverse_bio_dict = self.lca.reverse_dict()        
    99    262.6 MiB      0.0 MiB           self.cutoff = abs(self.lca.score) * self.cutoff_value
   100                                             
   101                                     #logs
   102    262.6 MiB      0.0 MiB           self.log.info("Starting dynamic LCA")
   103    262.6 MiB      0.0 MiB           self.log.info("Demand: %s" % self.demand)
   104    262.6 MiB      0.0 MiB           self.log.info("Worst case method: %s" % str(self.worst_case_method))
   105    262.6 MiB      0.0 MiB           self.log.info("Start datetime: %s" % self.t0)
   106    262.6 MiB      0.0 MiB           self.log.info("Maximum calculations: %i" % self.max_calc_number)
   107    262.6 MiB      0.0 MiB           self.log.info("Worst case LCA score: %.4g." % self.lca.score)
   108    262.6 MiB      0.0 MiB           self.log.info("Cutoff value (fraction): %.4g." % self.cutoff_value)
   109    262.6 MiB      0.0 MiB           self.log.info("Cutoff score: %.4g." % self.cutoff)
   110                             
   111                             
   112                                     # Initialize heap
   113                                     #MAYBE NOT NECESSARY ANYMORE
   114    262.6 MiB      0.0 MiB           heappush(
   115    262.6 MiB      0.0 MiB               self.heap,
   116                                         (
   117    262.6 MiB      0.0 MiB                   None,
   118    262.6 MiB      0.0 MiB                   ("Functional unit","Functional unit",), 
   119    262.6 MiB      0.0 MiB                   self.t0,
   120    262.6 MiB      0.0 MiB                   TemporalDistribution(
   121    262.6 MiB      0.0 MiB                       np.array([0,],dtype='timedelta64[s]'), # need int
   122    262.6 MiB      0.0 MiB                       np.array((1.,)).astype(float)                     
   123                                             ),
   124    262.6 MiB      0.0 MiB                   'Functional unit' #with tag
   125                                         )
   126                                     ) #if self.lca.score!=0 else self.timeline.add(self.t0.astype(datetime.datetime) , None, None,0) #deal with demand with no impact (doing so does not return error in LCIA)
   127                                     #TODO: the part commented out above was needed for `MultiDynamicLCA`, in commits `traverse also when total score is 0` this has been deleted, check if `MultiDynamicLCA` works fine or is affected
   128                             
   129    276.0 MiB      0.1 MiB           while self.heap:
   130    276.0 MiB      0.0 MiB               if self.calc_number >= self.max_calc_number:
   131                                             warnings.warn("Stopping traversal due to calculation count.")
   132                                             break
   133    276.0 MiB     13.3 MiB               self._iterate()
   134                                     
   135    276.0 MiB      0.0 MiB           self.log.info("NODES: " + pprint.pformat(self.nodes))
   136    276.0 MiB      0.0 MiB           self.log.info("EDGES: " + pprint.pformat(self.edges))    
   137                                     
   138    276.0 MiB      0.0 MiB           return self.timeline