         3613799 function calls (3566745 primitive calls) in 17.240 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
       38   12.889    0.339   16.144    0.425 dynamic_lca.py:260(_add_biosphere_flows)
  1579970    0.911    0.000    0.911    0.000 temporal_distribution.py:107(__iter__)
       69    0.530    0.008    0.535    0.008 pardiso_wrapper.py:238(_call_pardiso)
   142179    0.517    0.000    0.767    0.000 temporal_distribution.py:20(__init__)
   284723    0.430    0.000    0.430    0.000 {method 'astype' of 'numpy.ndarray' objects}
    47329    0.251    0.000    0.680    0.000 temporal_distribution.py:134(timedelta_to_datetime)
      106    0.189    0.002    0.189    0.002 {built-in method scipy.sparse._sparsetools.csr_matmat_pass2}
    47417    0.175    0.000    0.503    0.000 temporal_distribution.py:48(__mul__)
    47366    0.149    0.000    0.405    0.000 temporal_distribution.py:66(__div__)
    47329    0.120    0.000    1.724    0.000 dynamic_lca.py:363(_calculate_bio_td_datetime)
      106    0.084    0.001    0.084    0.001 {built-in method scipy.sparse._sparsetools.csr_matmat_pass1}
   549622    0.080    0.000    0.080    0.000 {built-in method builtins.isinstance}
    69936    0.067    0.000    0.067    0.000 {built-in method __new__ of type object at 0x7f1c10586760}
      408    0.049    0.000    0.054    0.000 numeric.py:2565(array_equal)
       30    0.044    0.001    0.148    0.005 dynamic_lca.py:327(<listcomp>)
    65506    0.038    0.000    0.126    0.000 timeline.py:38(add)
        4    0.034    0.009    0.034    0.009 {built-in method numpy.core.multiarray.lexsort}
     5644    0.027    0.000    0.027    0.000 {method 'reduce' of 'numpy.ufunc' objects}
     2617    0.026    0.000    0.050    0.000 compressed.py:876(_get_single_element)
  35049/1    0.025    0.000    0.044    0.044 copy.py:132(deepcopy)
        3    0.021    0.007    0.021    0.007 {method 'searchsorted' of 'numpy.ndarray' objects}
     7880    0.021    0.000    0.021    0.000 {built-in method numpy.core.multiarray.array}
    47366    0.020    0.000    0.425    0.000 temporal_distribution.py:76(__truediv__)
        2    0.020    0.010    0.022    0.011 indexing.py:10(index_with_arrays)
       68    0.019    0.000    0.031    0.000 dia.py:345(tocoo)
      123    0.015    0.000    0.015    0.000 {method 'sort' of 'numpy.ndarray' objects}
      130    0.014    0.000    0.014    0.000 {built-in method numpy.core.multiarray.concatenate}
        3    0.012    0.004    0.063    0.021 indexing.py:49(index_with_searchsorted)
       52    0.012    0.000    0.017    0.000 {_consolidate.consolidate}
        4    0.011    0.003    0.051    0.013 coo.py:460(_sum_duplicates)
     5494    0.010    0.000    0.016    0.000 sputils.py:188(isintlike)
     2647    0.010    0.000    0.036    0.000 sputils.py:265(_unpack_index)
    37153    0.010    0.000    0.010    0.000 indexing.py:72(<genexpr>)
        1    0.009    0.009    0.013    0.013 matrices.py:172(select_technosphere_array)
    24900    0.009    0.000    0.020    0.000 _collections_abc.py:742(__iter__)
11075/160    0.009    0.000    0.110    0.001 peewee.py:539(sql)
    81388    0.009    0.000    0.009    0.000 {method 'get' of 'dict' objects}
       34    0.008    0.000    0.008    0.000 {method 'reduceat' of 'numpy.ufunc' objects}
    25072    0.008    0.000    0.011    0.000 serialization.py:139(__getitem__)
    83477    0.008    0.000    0.008    0.000 {method 'append' of 'list' objects}
        2    0.008    0.004    0.008    0.004 {method 'take' of 'numpy.ndarray' objects}
     3075    0.008    0.000    0.013    0.000 peewee.py:459(__call__)
        6    0.008    0.001    0.008    0.001 {built-in method numpy.core.multiarray.fromfile}
        1    0.007    0.007    0.044    0.044 copy.py:236(_deepcopy_dict)
       72    0.007    0.000    0.007    0.000 {built-in method scipy.sparse._sparsetools.coo_tocsr}
     2647    0.007    0.000    0.014    0.000 sputils.py:331(_check_boolean)
     1607    0.006    0.000    0.059    0.000 peewee.py:1075(__sql__)
     6292    0.006    0.000    0.006    0.000 {built-in method builtins.hasattr}
     2617    0.006    0.000    0.006    0.000 {method 'compress' of 'numpy.ndarray' objects}
     2647    0.005    0.000    0.111    0.000 csr.py:236(__getitem__)
     3075    0.005    0.000    0.020    0.000 peewee.py:509(__call__)
     3534    0.005    0.000    0.011    0.000 peewee.py:1285(__sql__)
      315    0.005    0.000    0.013    0.000 compressed.py:128(check_format)
     1080    0.004    0.000    0.010    0.000 sputils.py:119(get_index_dtype)
      160    0.004    0.000    0.004    0.000 {method 'execute' of 'sqlite3.Cursor' objects}
     4174    0.004    0.000    0.022    0.000 peewee.py:479(inner)
  494/160    0.004    0.000    0.029    0.000 peewee.py:1240(__sql__)
        1    0.004    0.004    0.024    0.024 lca.py:181(<dictcomp>)
      218    0.004    0.000    0.004    0.000 {built-in method _pickle.loads}
     2647    0.004    0.000    0.004    0.000 sputils.py:293(_check_ellipsis)
     1080    0.003    0.000    0.003    0.000 getlimits.py:507(__init__)
      123    0.003    0.000    0.003    0.000 {method 'flatten' of 'numpy.ndarray' objects}
     5815    0.003    0.000    0.004    0.000 numeric.py:2135(isscalar)
     5611    0.003    0.000    0.005    0.000 <frozen importlib._bootstrap>:402(parent)
     3075    0.003    0.000    0.005    0.000 peewee.py:528(__exit__)
      156    0.003    0.000    0.004    0.000 peewee.py:6124(_initialize_columns)
      123    0.003    0.000    0.022    0.000 arraysetops.py:250(_unique1d)
      494    0.003    0.000    0.065    0.000 peewee.py:1433(__sql__)
      160    0.003    0.000    0.110    0.001 peewee.py:1933(__sql__)
     2087    0.003    0.000    0.003    0.000 contextlib.py:59(__init__)
     1607    0.003    0.000    0.018    0.000 peewee.py:677(apply_column)
     9767    0.003    0.000    0.004    0.000 peewee.py:547(literal)
        1    0.003    0.003    0.003    0.003 lca.py:183(<dictcomp>)
     6421    0.003    0.000    0.003    0.000 peewee.py:474(__getattr__)
        6    0.003    0.000    0.003    0.000 {built-in method numpy.core.multiarray.where}
     3242    0.003    0.000    0.005    0.000 peewee.py:454(__new__)
        1    0.003    0.003    0.003    0.003 lca.py:186(<dictcomp>)
    35319    0.003    0.000    0.003    0.000 {built-in method builtins.id}
       38    0.003    0.000   16.643    0.438 dynamic_lca.py:144(_iterate)
     1767    0.003    0.000    0.004    0.000 peewee.py:422(add)
      167    0.002    0.000    0.003    0.000 function_base.py:1843(diff)
     3534    0.002    0.000    0.002    0.000 {playhouse._speedups.quote}
    35048    0.002    0.000    0.002    0.000 copy.py:190(_deepcopy_atomic)
     5713    0.002    0.000    0.007    0.000 sputils.py:183(isscalarlike)
     3534    0.002    0.000    0.005    0.000 peewee.py:1273(__init__)
      102    0.002    0.000    0.009    0.000 coo.py:212(_check)
        1    0.002    0.002    0.009    0.009 matrices.py:183(select_biosphere_array)
     1607    0.002    0.000    0.003    0.000 peewee.py:3770(column)
     1767    0.002    0.000    0.023    0.000 peewee.py:837(__sql__)
      106    0.002    0.000    0.334    0.003 compressed.py:515(_mul_sparse_matrix)
     8856    0.002    0.000    0.002    0.000 peewee.py:497(scope)
       34    0.002    0.000    0.002    0.000 {method 'nonzero' of 'numpy.ndarray' objects}
     2087    0.002    0.000    0.007    0.000 contextlib.py:85(__exit__)
      626    0.002    0.000    0.004    0.000 peewee.py:551(value)
  315/247    0.002    0.000    0.058    0.000 compressed.py:25(__init__)
     2780    0.002    0.000    0.013    0.000 {method 'sum' of 'numpy.ndarray' objects}
     2617    0.002    0.000    0.010    0.000 fromnumeric.py:1610(compress)
      113    0.002    0.000    0.002    0.000 {built-in method scipy.sparse._sparsetools.csr_matvec}
     5617    0.002    0.000    0.007    0.000 <frozen importlib._bootstrap>:989(_handle_fromlist)
      182    0.002    0.000    0.002    0.000 {built-in method numpy.core.multiarray.copyto}
      315    0.002    0.000    0.004    0.000 compressed.py:1065(prune)
     5611    0.002    0.000    0.002    0.000 {method 'rpartition' of 'str' objects}
      283    0.002    0.000    0.002    0.000 {built-in method numpy.core.multiarray.zeros}
     5964    0.002    0.000    0.003    0.000 base.py:1111(isspmatrix)
     4206    0.002    0.000    0.023    0.000 {built-in method builtins.next}
     6150    0.002    0.000    0.002    0.000 peewee.py:501(parentheses)
     3534    0.002    0.000    0.003    0.000 peewee.py:1274(<listcomp>)
     5180    0.001    0.000    0.001    0.000 {built-in method builtins.getattr}
      160    0.001    0.000    0.005    0.000 peewee.py:5758(__init__)
      219    0.001    0.000    0.341    0.002 base.py:342(__mul__)
      533    0.001    0.000    0.001    0.000 {built-in method numpy.core.multiarray.empty}
     9334    0.001    0.000    0.001    0.000 {built-in method builtins.len}
     3075    0.001    0.000    0.002    0.000 peewee.py:523(__enter__)
       68    0.001    0.000    0.009    0.000 dia.py:78(__init__)
     4574    0.001    0.000    0.017    0.000 _methods.py:31(_sum)
     2624    0.001    0.000    0.030    0.000 fromnumeric.py:55(_wrapfunc)
       68    0.001    0.000    0.001    0.000 {built-in method numpy.core.multiarray.arange}
     5580    0.001    0.000    0.004    0.000 numeric.py:463(asarray)
      552    0.001    0.000    0.001    0.000 __init__.py:484(cast)
      582    0.001    0.000    0.003    0.000 tokenize.py:492(_tokenize)
     1607    0.001    0.000    0.065    0.000 peewee.py:3786(__sql__)
      218    0.001    0.000    0.007    0.000 peewee.py:6190(process_row)
     2087    0.001    0.000    0.005    0.000 contextlib.py:157(helper)
      137    0.001    0.000    0.007    0.000 pardiso_wrapper.py:185(_check_A)
       72    0.001    0.000    0.067    0.001 coo.py:301(tocsr)
      146    0.001    0.000    0.010    0.000 database.py:66(_get_queryset)
       68    0.001    0.000    0.935    0.014 lca.py:339(lci_calculation)
      485    0.001    0.000    0.001    0.000 base.py:77(set_shape)
      378    0.001    0.000    0.001    0.000 {method 'fetchone' of 'sqlite3.Cursor' objects}
        1    0.001    0.001    0.001    0.001 lca.py:201(<dictcomp>)
      379    0.001    0.000    0.002    0.000 sputils.py:200(isshape)
        4    0.001    0.000    0.001    0.000 {method 'copy' of 'numpy.ndarray' objects}
      218    0.001    0.000    0.011    0.000 peewee.py:6232(process_row)
     5579    0.001    0.000    0.001    0.000 base.py:100(get_shape)
      146    0.001    0.000    0.141    0.001 database.py:130(get)
     2212    0.001    0.000    0.002    0.000 peewee.py:349(<lambda>)
        1    0.001    0.001    0.001    0.001 lca.py:200(<dictcomp>)
        1    0.001    0.001    0.001    0.001 matrices.py:190(get_technosphere_inputs_mask)
      160    0.001    0.000    0.007    0.000 peewee.py:2563(execute_sql)
     3694    0.001    0.000    0.001    0.000 peewee.py:418(mapping)
     3396    0.001    0.000    0.001    0.000 data.py:25(_get_dtype)
      218    0.001    0.000    0.003    0.000 peewee.py:5222(__init__)
     3534    0.001    0.000    0.001    0.000 {method 'replace' of 'str' objects}
      102    0.001    0.000    0.022    0.000 coo.py:118(__init__)
      378    0.001    0.000    0.017    0.000 peewee.py:3535(iterate)
      612    0.001    0.000    0.002    0.000 peewee.py:1859(clone)
     3871    0.001    0.000    0.001    0.000 csr.py:231(_swap)
  685/542    0.001    0.000    0.001    0.000 defmatrix.py:258(__array_finalize__)
     1672    0.001    0.000    0.001    0.000 peewee.py:3647(__set__)
     1767    0.001    0.000    0.006    0.000 peewee.py:435(__getitem__)
     1579    0.001    0.000    0.002    0.000 base.py:193(nnz)
      146    0.001    0.000    0.143    0.001 utils.py:329(get_activity)
      612    0.001    0.000    0.005    0.000 peewee.py:596(inner)
      143    0.001    0.000    0.020    0.000 compressed.py:604(sum)
     1464    0.001    0.000    0.001    0.000 _collections_abc.py:657(get)
     2216    0.001    0.000    0.001    0.000 inspect.py:73(isclass)
     1672    0.001    0.000    0.002    0.000 {built-in method builtins.setattr}
     1261    0.001    0.000    0.001    0.000 compressed.py:100(getnnz)
      113    0.001    0.000    0.011    0.000 base.py:825(sum)
      570    0.001    0.000    0.001    0.000 {method 'match' of '_sre.SRE_Pattern' objects}
     1767    0.001    0.000    0.005    0.000 peewee.py:428(get)
      146    0.001    0.000    0.014    0.000 peewee.py:3558(fill_cache)
       68    0.001    0.000    0.002    0.000 shape_base.py:826(tile)
        6    0.001    0.000    0.001    0.000 tokenize.py:243(untokenize)
        1    0.001    0.001    0.002    0.002 matrices.py:204(fix_supply_use)
  640/626    0.001    0.000    0.001    0.000 peewee.py:1169(__init__)
     2087    0.001    0.000    0.019    0.000 contextlib.py:79(__enter__)
      167    0.001    0.000    0.001    0.000 peewee.py:487(__init__)
     1080    0.001    0.000    0.001    0.000 getlimits.py:532(max)
       51    0.001    0.000    0.006    0.000 dynamic_lca.py:399(_get_temporal_distribution)
     1330    0.001    0.000    0.001    0.000 {method 'copy' of 'dict' objects}
      485    0.001    0.000    0.001    0.000 base.py:70(__init__)
      320    0.001    0.000    0.001    0.000 peewee.py:1003(__eq__)
     1461    0.001    0.000    0.001    0.000 peewee.py:232(__getattr__)
        1    0.001    0.001    0.281    0.281 lca.py:209(load_lci_data)
      160    0.001    0.000    0.123    0.001 peewee.py:1745(_execute)
        1    0.001    0.001   17.257   17.257 dynamic_lca.py:83(calculate)
      318    0.001    0.000    0.001    0.000 coo.py:186(getnnz)
       67    0.001    0.000    0.612    0.009 lca.py:492(redo_lci)
     1454    0.001    0.000    0.001    0.000 peewee.py:3780(python_value)
       51    0.001    0.000    0.002    0.000 numeric.py:2522(within_tol)
      612    0.001    0.000    0.001    0.000 peewee.py:586(clone)
       68    0.001    0.000    0.252    0.004 pardiso_wrapper.py:132(solve)
     3075    0.001    0.000    0.001    0.000 {method 'pop' of 'list' objects}
     3694    0.001    0.000    0.001    0.000 peewee.py:699(__hash__)
     1607    0.001    0.000    0.001    0.000 peewee.py:1062(__init__)
      152    0.001    0.000    0.001    0.000 database.py:13(DatabaseChooser)
      308    0.001    0.000    0.001    0.000 {method 'view' of 'numpy.ndarray' objects}
       68    0.001    0.000    0.598    0.009 scipy_aliases.py:12(spsolve)
      612    0.001    0.000    0.003    0.000 peewee.py:5774(clone)
      378    0.001    0.000    0.017    0.000 peewee.py:3619(next)
       30    0.001    0.000    0.001    0.000 {built-in method scipy.sparse._sparsetools.get_csr_submatrix}
      417    0.001    0.000    0.001    0.000 sputils.py:91(to_native)
     1923    0.001    0.000    0.001    0.000 peewee.py:4907(table)
        6    0.001    0.000    0.001    0.000 {built-in method io.open}
      160    0.000    0.000    0.120    0.001 peewee.py:2586(execute)
        6    0.000    0.000    0.000    0.000 {built-in method builtins.compile}
      146    0.000    0.000    0.001    0.000 proxies.py:84(__init__)
      320    0.000    0.000    0.002    0.000 peewee.py:668(apply_alias)
      136    0.000    0.000    0.054    0.000 pardiso_wrapper.py:173(_csr_matrix_equal)
1148/1088    0.000    0.000    0.000    0.000 proxies.py:81(__getitem__)
      143    0.000    0.000    0.003    0.000 defmatrix.py:391(sum)
      160    0.000    0.000    0.007    0.000 peewee.py:1694(_apply_ordering)
       68    0.000    0.000    0.002    0.000 lca.py:128(build_demand_array)
      152    0.000    0.000    0.001    0.000 database.py:41(__init__)
      160    0.000    0.000    0.002    0.000 peewee.py:1838(__init__)
  640/626    0.000    0.000    0.004    0.000 peewee.py:1181(__sql__)
     1505    0.000    0.000    0.001    0.000 peewee.py:3903(adapt)
      485    0.000    0.000    0.001    0.000 data.py:22(__init__)
      552    0.000    0.000    0.000    0.000 _internal.py:241(__init__)
     1139    0.000    0.000    0.001    0.000 peewee.py:3642(__get__)
      650    0.000    0.000    0.007    0.000 {method 'all' of 'numpy.ndarray' objects}
      160    0.000    0.000    0.002    0.000 peewee.py:5652(_get_cursor_wrapper)
        1    0.000    0.000    0.000    0.000 lca.py:189(<dictcomp>)
      113    0.000    0.000    0.003    0.000 compressed.py:489(_mul_vector)
      612    0.000    0.000    0.001    0.000 peewee.py:1544(clone)
      630    0.000    0.000    0.000    0.000 _util.py:128(_prune_array)
      213    0.000    0.000    0.000    0.000 {built-in method numpy.core.multiarray.empty_like}
       68    0.000    0.000    0.010    0.000 construct.py:26(spdiags)
      480    0.000    0.000    0.001    0.000 peewee.py:1445(CommaNodeList)
      256    0.000    0.000    0.002    0.000 defmatrix.py:212(__new__)
      160    0.000    0.000    0.001    0.000 peewee.py:6227(__init__)
      256    0.000    0.000    0.002    0.000 defmatrix.py:32(asmatrix)
       37    0.000    0.000    0.018    0.000 dynamic_lca.py:384(_calculate_new_td)
      160    0.000    0.000    0.002    0.000 peewee.py:2604(get_sql_context)
   122/50    0.000    0.000    0.001    0.000 {method 'format' of 'str' objects}
      553    0.000    0.000    0.000    0.000 {built-in method builtins.max}
       30    0.000    0.000    0.003    0.000 compressed.py:949(tocoo)
      265    0.000    0.000    0.001    0.000 __init__.py:1542(isEnabledFor)
      160    0.000    0.000    0.006    0.000 peewee.py:5244(select)
      146    0.000    0.000    0.128    0.001 peewee.py:5719(get)
       68    0.000    0.000    0.042    0.001 base.py:758(tocsr)
      417    0.000    0.000    0.000    0.000 {method 'newbyteorder' of 'numpy.dtype' objects}
      306    0.000    0.000    0.001    0.000 {built-in method _functools.reduce}
      160    0.000    0.000    0.002    0.000 peewee.py:5915(_get_model_cursor_wrapper)
        6    0.000    0.000    0.005    0.001 format.py:425(_filter_header)
  867/862    0.000    0.000    0.000    0.000 {built-in method builtins.issubclass}
      552    0.000    0.000    0.002    0.000 _internal.py:253(data_as)
      160    0.000    0.000    0.000    0.000 peewee.py:1533(__init__)
     1238    0.000    0.000    0.000    0.000 {method 'find' of 'str' objects}
      306    0.000    0.000    0.001    0.000 peewee.py:1665(where)
      160    0.000    0.000    0.000    0.000 peewee.py:2591(get_context_options)
      654    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
      321    0.000    0.000    0.000    0.000 {method 'reshape' of 'numpy.ndarray' objects}
       30    0.000    0.000    0.006    0.000 compressed.py:633(_minor_reduce)
      218    0.000    0.000    0.004    0.000 sqlite.py:19(python_value)
      160    0.000    0.000    0.002    0.000 peewee.py:5647(__init__)
      787    0.000    0.000    0.001    0.000 numeric.py:534(asanyarray)
       51    0.000    0.000    0.003    0.000 numeric.py:2463(isclose)
       68    0.000    0.000    0.000    0.000 shape_base.py:63(atleast_2d)
      160    0.000    0.000    0.000    0.000 peewee.py:6119(__init__)
   140/64    0.000    0.000    0.069    0.001 pprint.py:490(_safe_repr)
     1692    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
      265    0.000    0.000    0.000    0.000 __init__.py:1528(getEffectiveLevel)
      123    0.000    0.000    0.023    0.000 arraysetops.py:113(unique)
      570    0.000    0.000    0.000    0.000 tokenize.py:230(add_whitespace)
       30    0.000    0.000    0.004    0.000 csr.py:411(_get_submatrix)
      160    0.000    0.000    0.001    0.000 peewee.py:1651(__init__)
        2    0.000    0.000    0.028    0.014 utils.py:23(load_arrays)
      113    0.000    0.000    0.012    0.000 lca.py:412(score)
      160    0.000    0.000    0.000    0.000 {method 'cursor' of 'sqlite3.Connection' objects}
      146    0.000    0.000    0.000    0.000 peewee.py:1307(__init__)
      146    0.000    0.000    0.015    0.000 peewee.py:3513(__getitem__)
      353    0.000    0.000    0.000    0.000 {method 'ravel' of 'numpy.ndarray' objects}
      494    0.000    0.000    0.000    0.000 peewee.py:1234(__init__)
    279/6    0.000    0.000    0.000    0.000 ast.py:51(_convert)
      105    0.000    0.000    0.001    0.000 utils.py:190(wrap_functional_unit)
      494    0.000    0.000    0.000    0.000 peewee.py:1424(__init__)
      650    0.000    0.000    0.006    0.000 _methods.py:40(_all)
      419    0.000    0.000    0.000    0.000 sputils.py:227(isdense)
     1252    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
      144    0.000    0.000    0.000    0.000 base.py:562(__getattr__)
       68    0.000    0.000    0.599    0.009 lca.py:295(solve_linear_system)
       86    0.000    0.000    0.016    0.000 proxies.py:75(__iter__)
      160    0.000    0.000    0.001    0.000 peewee.py:684(__init__)
      105    0.000    0.000    0.000    0.000 utils.py:196(<listcomp>)
      208    0.000    0.000    0.003    0.000 {method 'max' of 'numpy.ndarray' objects}
      179    0.000    0.000    0.000    0.000 sputils.py:20(upcast)
      212    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
      160    0.000    0.000    0.057    0.000 peewee.py:6003(__sql_selection__)
       36    0.000    0.000    0.001    0.000 proxies.py:192(valid)
      160    0.000    0.000    0.001    0.000 peewee.py:646(__init__)
      113    0.000    0.000    0.000    0.000 defmatrix.py:280(__getitem__)
      570    0.000    0.000    0.001    0.000 tokenize.py:152(_compile)
       14    0.000    0.000    0.000    0.000 {built-in method _warnings.warn}
      584    0.000    0.000    0.000    0.000 re.py:286(_compile)
      143    0.000    0.000    0.000    0.000 numerictypes.py:728(issubdtype)
      102    0.000    0.000    0.001    0.000 numeric.py:2667(seterr)
       72    0.000    0.000    0.000    0.000 proxies.py:291(__init__)
      160    0.000    0.000    0.001    0.000 peewee.py:2558(cursor)
      935    0.000    0.000    0.000    0.000 proxies.py:36(__getitem__)
       38    0.000    0.000    0.002    0.000 dynamic_lca.py:431(_get_scale_value)
      136    0.000    0.000    0.055    0.000 pardiso_wrapper.py:166(_is_already_factorized)
       37    0.000    0.000    0.343    0.009 dynamic_lca.py:421(_discard_node)
        1    0.000    0.000    0.000    0.000 {built-in method scipy.sparse._sparsetools.csr_has_sorted_indices}
      160    0.000    0.000    0.000    0.000 peewee.py:2657(in_transaction)
      137    0.000    0.000    0.000    0.000 pardiso_wrapper.py:282(set_iparm)
      167    0.000    0.000    0.000    0.000 peewee.py:441(push)
        6    0.000    0.000    0.006    0.001 format.py:463(_read_array_header)
      102    0.000    0.000    0.000    0.000 numeric.py:2767(geterr)
      160    0.000    0.000    0.123    0.001 peewee.py:1519(inner)
    64/38    0.000    0.000    0.070    0.002 pprint.py:154(_format)
       37    0.000    0.000    0.338    0.009 lca.py:509(redo_lcia)
       38    0.000    0.000    0.000    0.000 temporal_distribution.py:115(__str__)
      143    0.000    0.000    0.001    0.000 sputils.py:172(get_sum_dtype)
      146    0.000    0.000    0.000    0.000 peewee.py:1336(__sql__)
      174    0.000    0.000    0.042    0.000 base.py:249(asformat)
      576    0.000    0.000    0.000    0.000 <string>:12(__new__)
      117    0.000    0.000    0.000    0.000 fromnumeric.py:1380(ravel)
       30    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
       38    0.000    0.000    0.010    0.000 lca.py:369(lcia_calculation)
       68    0.000    0.000    0.000    0.000 pardiso_wrapper.py:214(_check_b)
       69    0.000    0.000    0.001    0.000 numeric.py:87(zeros_like)
      206    0.000    0.000    0.000    0.000 {built-in method builtins.all}
        1    0.000    0.000    0.075    0.075 lca.py:156(fix_dictionaries)
      167    0.000    0.000    0.000    0.000 peewee.py:411(__init__)
      163    0.000    0.000    0.001    0.000 temporal_distribution.py:111(total)
      160    0.000    0.000    0.000    0.000 peewee.py:1742(_get_hash)
      108    0.000    0.000    0.001    0.000 fromnumeric.py:1973(all)
      570    0.000    0.000    0.000    0.000 re.py:231(compile)
      327    0.000    0.000    0.000    0.000 peewee.py:3777(db_value)
      106    0.000    0.000    0.000    0.000 compressed.py:117(_set_self)
      206    0.000    0.000    0.002    0.000 {method 'min' of 'numpy.ndarray' objects}
      113    0.000    0.000    0.001    0.000 numeric.py:150(ones)
       72    0.000    0.000    0.001    0.000 proxies.py:54(__str__)
      431    0.000    0.000    0.000    0.000 {built-in method builtins.hash}
      160    0.000    0.000    0.000    0.000 peewee.py:3500(__init__)
       77    0.000    0.000    0.000    0.000 shape_base.py:11(atleast_1d)
      208    0.000    0.000    0.003    0.000 _methods.py:25(_amax)
      207    0.000    0.000    0.000    0.000 {built-in method _ctypes.POINTER}
      105    0.000    0.000    0.000    0.000 __init__.py:1296(info)
        1    0.000    0.000    0.000    0.000 lca.py:202(<dictcomp>)
      299    0.000    0.000    0.000    0.000 serialization.py:149(__contains__)
      216    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
       72    0.000    0.000    0.000    0.000 proxies.py:93(valid)
      146    0.000    0.000    0.000    0.000 peewee.py:1687(paginate)
       30    0.000    0.000    0.004    0.000 csr.py:368(_get_row_slice)
      160    0.000    0.000    0.000    0.000 peewee.py:438(__setitem__)
      177    0.000    0.000    0.000    0.000 {built-in method builtins.abs}
       36    0.000    0.000    0.069    0.002 proxies.py:125(__str__)
        6    0.000    0.000    0.000    0.000 {built-in method posix.stat}
       72    0.000    0.000    0.033    0.000 proxies.py:139(_get_input)
     1238    0.000    0.000    0.000    0.000 peewee.py:609(unwrap)
        6    0.000    0.000    0.015    0.002 npyio.py:266(load)
      143    0.000    0.000    0.000    0.000 defmatrix.py:357(_collapse)
      146    0.000    0.000    0.000    0.000 peewee.py:1316(decorator)
      160    0.000    0.000    0.000    0.000 peewee.py:693(_update_hash)
      160    0.000    0.000    0.123    0.001 peewee.py:1594(execute)
      134    0.000    0.000    0.000    0.000 proxies.py:109(key)
      160    0.000    0.000    0.000    0.000 __init__.py:1284(debug)
       60    0.000    0.000    0.000    0.000 csr.py:416(process_slice)
      174    0.000    0.000    0.000    0.000 peewee.py:982(inner)
       38    0.000    0.000    0.070    0.002 pprint.py:142(pformat)
       38    0.000    0.000    0.070    0.002 pprint.py:55(pformat)
        1    0.000    0.000    0.206    0.206 matrices.py:139(build)
      137    0.000    0.000    0.000    0.000 compressed.py:1025(__get_sorted)
      552    0.000    0.000    0.000    0.000 {built-in method _ctypes.byref}
       69    0.000    0.000    0.000    0.000 numeric.py:586(ascontiguousarray)
      167    0.000    0.000    0.000    0.000 peewee.py:576(query)
      269    0.000    0.000    0.000    0.000 {method 'pop' of 'dict' objects}
       90    0.000    0.000    0.000    0.000 proxies.py:78(__hash__)
       38    0.000    0.000    0.000    0.000 {built-in method _heapq.heappop}
      206    0.000    0.000    0.002    0.000 _methods.py:28(_amin)
       38    0.000    0.000    0.000    0.000 pprint.py:99(__init__)
      143    0.000    0.000    0.000    0.000 numerictypes.py:660(issubclass_)
      309    0.000    0.000    0.000    0.000 {method 'lower' of 'str' objects}
      570    0.000    0.000    0.000    0.000 {method 'span' of '_sre.SRE_Match' objects}
       30    0.000    0.000    0.000    0.000 {built-in method scipy.sparse._sparsetools.expandptr}
      218    0.000    0.000    0.000    0.000 {method 'clear' of 'set' objects}
       68    0.000    0.000    0.000    0.000 {method 'squeeze' of 'numpy.ndarray' objects}
      160    0.000    0.000    0.000    0.000 peewee.py:3612(__init__)
      153    0.000    0.000    0.000    0.000 data_store.py:32(__init__)
      105    0.000    0.000    0.069    0.001 {built-in method builtins.repr}
       36    0.000    0.000    0.033    0.001 proxies.py:160(_get_output)
      146    0.000    0.000    0.000    0.000 peewee.py:1315(__getattr__)
       14    0.000    0.000    0.000    0.000 proxies.py:45(__init__)
        6    0.000    0.000    0.014    0.002 format.py:595(read_array)
      137    0.000    0.000    0.000    0.000 csr.py:458(isspmatrix_csr)
       64    0.000    0.000    0.069    0.001 pprint.py:391(_repr)
      102    0.000    0.000    0.000    0.000 {built-in method numpy.core.umath.seterrobj}
      136    0.000    0.000    0.000    0.000 shape_base.py:897(<genexpr>)
      113    0.000    0.000    0.000    0.000 sputils.py:54(upcast_char)
       51    0.000    0.000    0.000    0.000 numeric.py:3060(__init__)
       30    0.000    0.000    0.001    0.000 numeric.py:859(flatnonzero)
       51    0.000    0.000    0.000    0.000 numeric.py:3069(__exit__)
      160    0.000    0.000    0.000    0.000 peewee.py:1706(__sql__)
       24    0.000    0.000    0.000    0.000 {method 'read' of '_io.BufferedReader' objects}
       68    0.000    0.000    0.000    0.000 dia.py:377(isspmatrix_dia)
       68    0.000    0.000    0.000    0.000 csc.py:220(isspmatrix_csc)
       51    0.000    0.000    0.000    0.000 numeric.py:3064(__enter__)
       51    0.000    0.000    0.000    0.000 {built-in method numpy.core.multiarray.result_type}
       72    0.000    0.000    0.051    0.001 coo.py:449(sum_duplicates)
        4    0.000    0.000    0.070    0.017 matrices.py:117(build_matrix)
      160    0.000    0.000    0.000    0.000 peewee.py:2550(is_closed)
        6    0.000    0.000    0.000    0.000 {method 'close' of '_io.BufferedReader' objects}
       14    0.000    0.000    0.001    0.000 proxies.py:72(_get_queryset)
      160    0.000    0.000    0.000    0.000 peewee.py:505(subquery)
       38    0.000    0.000    0.000    0.000 {built-in method _heapq.heappush}
        6    0.000    0.000    0.001    0.000 utils.py:1070(safe_eval)
       36    0.000    0.000    0.033    0.001 proxies.py:224(unit)
       14    0.000    0.000    0.000    0.000 filesystem.py:13(safe_filename)
       30    0.000    0.000    0.000    0.000 sputils.py:71(downcast_intp_index)
       37    0.000    0.000    0.000    0.000 abc.py:178(__instancecheck__)
       30    0.000    0.000    0.000    0.000 defmatrix.py:1036(getT)
      160    0.000    0.000    0.000    0.000 peewee.py:2370(__exit__)
       69    0.000    0.000    0.000    0.000 pardiso_wrapper.py:316(set_phase)
       36    0.000    0.000    0.069    0.002 proxies.py:25(<lambda>)
      6/2    0.000    0.000    0.000    0.000 pprint.py:350(_format_items)
       41    0.000    0.000    0.000    0.000 _weakrefset.py:70(__contains__)
      120    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
       84    0.000    0.000    0.000    0.000 dynamic_lca.py:28(__getattr__)
       30    0.000    0.000    0.000    0.000 {method 'transpose' of 'numpy.ndarray' objects}
       64    0.000    0.000    0.069    0.001 pprint.py:400(format)
       10    0.000    0.000    0.000    0.000 {built-in method builtins.sorted}
       18    0.000    0.000    0.000    0.000 format.py:797(_read_bytes)
      204    0.000    0.000    0.000    0.000 {built-in method numpy.core.umath.geterrobj}
      160    0.000    0.000    0.000    0.000 peewee.py:1671(order_by)
      160    0.000    0.000    0.000    0.000 {method 'close' of 'sqlite3.Cursor' objects}
      386    0.000    0.000    0.000    0.000 {method 'isidentifier' of 'str' objects}
      3/1    0.000    0.000    0.000    0.000 abc.py:194(__subclasscheck__)
        1    0.000    0.000    0.002    0.002 matrices.py:37(build)
        2    0.000    0.000    0.015    0.007 utils.py:26(<listcomp>)
       12    0.000    0.000    0.000    0.000 posixpath.py:73(join)
       36    0.000    0.000    0.000    0.000 proxies.py:231(amount)
      146    0.000    0.000    0.000    0.000 database.py:100(_get_order_by)
       28    0.000    0.000    0.000    0.000 {method 'sub' of '_sre.SRE_Pattern' objects}
        4    0.000    0.000    0.000    0.000 function_base.py:5095(append)
       28    0.000    0.000    0.000    0.000 dynamic_lca.py:411(<genexpr>)
      160    0.000    0.000    0.000    0.000 peewee.py:2369(__enter__)
       60    0.000    0.000    0.000    0.000 csr.py:439(check_bounds)
       28    0.000    0.000    0.000    0.000 pprint.py:87(__lt__)
       30    0.000    0.000    0.000    0.000 {method 'indices' of 'slice' objects}
       30    0.000    0.000    0.000    0.000 proxies.py:69(__eq__)
      113    0.000    0.000    0.000    0.000 sputils.py:231(validateaxis)
        6    0.000    0.000    0.001    0.000 ast.py:40(literal_eval)
       38    0.000    0.000    0.000    0.000 {method 'getvalue' of '_io.StringIO' objects}
        7    0.000    0.000    0.000    0.000 proxies.py:230(biosphere)
        1    0.000    0.000    0.022    0.022 matrices.py:212(build_technosphere_matrix)
        1    0.000    0.000    0.315    0.315 pardiso_wrapper.py:110(factorize)
        1    0.000    0.000    0.000    0.000 lca.py:55(__init__)
       96    0.000    0.000    0.000    0.000 {method 'write' of '_io.StringIO' objects}
       84    0.000    0.000    0.000    0.000 dynamic_lca.py:25(fake_function)
       14    0.000    0.000    0.011    0.001 peewee.py:5706(__iter__)
        6    0.000    0.000    0.000    0.000 format.py:201(read_magic)
        1    0.000    0.000   17.257   17.257 {built-in method builtins.exec}
        1    0.000    0.000    0.002    0.002 lca.py:233(load_lcia_data)
        6    0.000    0.000    0.001    0.000 tokenize.py:317(untokenize)
        3    0.000    0.000    0.021    0.007 fromnumeric.py:1022(searchsorted)
       24    0.000    0.000    0.000    0.000 ast.py:65(<genexpr>)
        4    0.000    0.000    0.000    0.000 numerictypes.py:942(_can_coerce_all)
       14    0.000    0.000    0.000    0.000 peewee.py:1449(EnclosedNodeList)
        8    0.000    0.000    0.000    0.000 utils.py:25(<genexpr>)
       14    0.000    0.000    0.000    0.000 peewee.py:3508(__iter__)
        3    0.000    0.000    0.000    0.000 shape_base.py:288(<listcomp>)
        3    0.000    0.000    0.013    0.004 shape_base.py:239(hstack)
        6    0.000    0.000    0.000    0.000 data_store.py:180(filepath_processed)
        7    0.000    0.000    0.000    0.000 proxies.py:219(exchanges)
        1    0.000    0.000    0.000    0.000 meta.py:107(clean)
        2    0.000    0.000    0.000    0.000 numerictypes.py:964(find_common_type)
        6    0.000    0.000    0.000    0.000 {built-in method _struct.unpack}
       28    0.000    0.000    0.000    0.000 {built-in method builtins.iter}
        1    0.000    0.000    0.002    0.002 lca.py:351(lcia)
        6    0.000    0.000    0.000    0.000 py3k.py:42(isfileobj)
        6    0.000    0.000    0.000    0.000 genericpath.py:27(isfile)
        8    0.000    0.000    0.000    0.000 _weakrefset.py:58(__iter__)
       15    0.000    0.000    0.000    0.000 {built-in method builtins.any}
        1    0.000    0.000    0.002    0.002 lca.py:194(reverse_dict)
        1    0.000    0.000    0.000    0.000 ia_data_store.py:11(abbreviate)
        7    0.000    0.000    0.000    0.000 peewee.py:573(parse)
        6    0.000    0.000    0.000    0.000 project.py:176(dir)
        2    0.000    0.000    0.000    0.000 pprint.py:224(_pprint_set)
        6    0.000    0.000    0.000    0.000 {method 'startswith' of 'bytes' objects}
        6    0.000    0.000    0.000    0.000 {method 'seek' of '_io.BufferedReader' objects}
        1    0.000    0.000    0.607    0.607 lca.py:315(lci)
       15    0.000    0.000    0.000    0.000 meta.py:118(<genexpr>)
       22    0.000    0.000    0.000    0.000 {built-in method numpy.core.multiarray.can_cast}
       12    0.000    0.000    0.000    0.000 {built-in method _hashlib.openssl_md5}
        1    0.000    0.000    0.000    0.000 __init__.py:1159(getLogger)
        6    0.000    0.000    0.000    0.000 tokenize.py:224(__init__)
        1    0.000    0.000    0.000    0.000 copy.py:252(_keep_alive)
       14    0.000    0.000    0.000    0.000 re.py:184(sub)
        2    0.000    0.000    0.000    0.000 base.py:169(<listcomp>)
        4    0.000    0.000    0.000    0.000 utils.py:71(get_filepaths)
        2    0.000    0.000    0.000    0.000 decorators.py:200(_build)
       14    0.000    0.000    0.000    0.000 numerictypes.py:951(<listcomp>)
        4    0.000    0.000    0.000    0.000 pprint.py:215(_pprint_tuple)
        3    0.000    0.000    0.000    0.000 _weakrefset.py:26(__exit__)
        6    0.000    0.000    0.000    0.000 {method 'decode' of 'bytes' objects}
        6    0.000    0.000    0.000    0.000 {built-in method builtins.min}
       12    0.000    0.000    0.000    0.000 {method 'read' of '_io.StringIO' objects}
        2    0.000    0.000    0.000    0.000 base.py:167(extend)
        4    0.000    0.000    0.002    0.000 fromnumeric.py:1487(nonzero)
        6    0.000    0.000    0.000    0.000 ast.py:30(parse)
       35    0.000    0.000    0.000    0.000 __init__.py:539(__missing__)
        1    0.000    0.000    0.000    0.000 _collections_abc.py:676(items)
        1    0.000    0.000    0.000    0.000 utils.py:69(<listcomp>)
        1    0.000    0.000    0.000    0.000 compressed.py:1085(_with_data)
        1    0.000    0.000    0.001    0.001 data.py:77(copy)
        1    0.000    0.000    0.000    0.000 __init__.py:1266(__init__)
        6    0.000    0.000    0.000    0.000 tokenize.py:729(generate_tokens)
        2    0.000    0.000    0.000    0.000 _weakrefset.py:36(__init__)
       12    0.000    0.000    0.000    0.000 {method 'encode' of 'str' objects}
        1    0.000    0.000    0.000    0.000 utils.py:81(clean_databases)
        2    0.000    0.000    0.000    0.000 decorators.py:225(_wrapper)
        5    0.000    0.000    0.000    0.000 base.py:120(filename)
        6    0.000    0.000    0.000    0.000 py3k.py:37(asstr)
       12    0.000    0.000    0.000    0.000 {method 'hexdigest' of '_hashlib.HASH' objects}
       14    0.000    0.000    0.000    0.000 pprint.py:84(__init__)
        1    0.000    0.000    0.000    0.000 __init__.py:1811(getLogger)
        8    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
       12    0.000    0.000    0.000    0.000 {built-in method posix.fspath}
        1    0.000    0.000    0.000    0.000 ia_data_store.py:57(get_abbreviation)
        1    0.000    0.000    0.000    0.000 ia_data_store.py:81(register)
        1    0.000    0.000    0.000    0.000 data_store.py:64(register)
        1    0.000    0.000    0.000    0.000 utils.py:68(<listcomp>)
        1    0.000    0.000   17.257   17.257 <string>:1(<module>)
        6    0.000    0.000    0.000    0.000 format.py:503(<listcomp>)
       14    0.000    0.000    0.000    0.000 {built-in method unicodedata.normalize}
        1    0.000    0.000    0.000    0.000 __init__.py:219(_acquireLock)
        1    0.000    0.000    0.000    0.000 timeline.py:29(__init__)
        1    0.000    0.000    0.000    0.000 ia_data_store.py:30(<listcomp>)
        1    0.000    0.000    0.000    0.000 data_store.py:40(_get_metadata)
        1    0.000    0.000    0.000    0.000 base.py:160(find_graph_dependents)
        1    0.000    0.000    0.000    0.000 utils.py:66(get_database_filepath)
        2    0.000    0.000    0.000    0.000 matrices.py:130(build_diagonal_matrix)
        2    0.000    0.000    0.000    0.000 serialization.py:179(__iter__)
        6    0.000    0.000    0.000    0.000 format.py:171(_check_version)
        2    0.000    0.000    0.000    0.000 numerictypes.py:1015(<listcomp>)
        1    0.000    0.000    0.000    0.000 __init__.py:683(__init__)
        1    0.000    0.000    0.000    0.000 __init__.py:1210(_fixupParents)
       12    0.000    0.000    0.000    0.000 posixpath.py:39(_get_sep)
        3    0.000    0.000    0.000    0.000 _weakrefset.py:81(add)
       18    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'acquire' of '_thread.RLock' objects}
        1    0.000    0.000    0.000    0.000 ia_data_store.py:27(<listcomp>)
        2    0.000    0.000    0.000    0.000 ia_data_store.py:28(<lambda>)
        1    0.000    0.000    0.000    0.000 meta.py:53(__len__)
        6    0.000    0.000    0.000    0.000 project.py:128(current)
        1    0.000    0.000    0.000    0.000 __init__.py:228(_releaseLock)
        1    0.000    0.000    0.000    0.000 _collections_abc.py:698(__init__)
        3    0.000    0.000    0.000    0.000 _weakrefset.py:16(__init__)
        3    0.000    0.000    0.000    0.000 _weakrefset.py:20(__enter__)
        3    0.000    0.000    0.000    0.000 _weakrefset.py:52(_commit_removals)
        2    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}
        2    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'rfind' of 'str' objects}
        6    0.000    0.000    0.000    0.000 {built-in method _stat.S_ISREG}
        1    0.000    0.000    0.000    0.000 lca.py:119(get_array_filepaths)
        1    0.000    0.000    0.000    0.000 ia_data_store.py:94(filename)
        2    0.000    0.000    0.000    0.000 numerictypes.py:1016(<listcomp>)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 __init__.py:190(_checkLevel)
        3    0.000    0.000    0.000    0.000 {method 'remove' of 'set' objects}
        3    0.000    0.000    0.000    0.000 {method '__subclasshook__' of 'object' objects}
        2    0.000    0.000    0.000    0.000 {method '__subclasses__' of 'type' objects}
        1    0.000    0.000    0.000    0.000 {method 'release' of '_thread.RLock' objects}