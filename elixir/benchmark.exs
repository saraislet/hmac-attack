# list = Enum.to_list(1..10)
# map_compare = fn i -> ElixirCompare.nc_compare_closure_diff(i,i) end

Benchee.run(%{
  # "compare_same"    => fn -> Enum.flat_map(list, ElixirCompare.nc_compare_closure_same()) end,
  # "compare_diff"    => fn -> Enum.flat_map(list, map_compare) end
  "compare_diff"    => fn -> ElixirCompare.nonconstant_compare("hiii!!11", "hiii!!11") end
})

