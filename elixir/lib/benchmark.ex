defmodule Benchmark do 

  def benchmark_compare(a, b) do
    Benchee.run(%{
      "compare_same" => fn -> ElixirCompare.nonconstant_compare(a, a) end,
      "compare_diff" => fn -> ElixirCompare.nonconstant_compare(a, b) end
    })
  end

  def benchmark_compare_repeat(a, b, c, d, n) do
    IO.puts("Comparing strings: #{a}, #{b}, #{c}, #{d}.")
    Benchee.run(%{
      "compare_aa" => fn -> ElixirCompare.repeat_compare(a, a, n) end,
      "compare_ab" => fn -> ElixirCompare.repeat_compare(a, b, n) end,
      "compare_ac" => fn -> ElixirCompare.repeat_compare(a, c, n) end,
      "compare_ad" => fn -> ElixirCompare.repeat_compare(a, d, n) end,
    })
  end

  def benchmark_compare_firstlast(a, b, c, n) do
    IO.puts("Comparing strings: #{a} to #{b} and #{c}.")
    Benchee.run(%{
      "compare_ab" => fn -> ElixirCompare.repeat_compare(a, b, n) end,
      "compare_ac" => fn -> ElixirCompare.repeat_compare(a, c, n) end,
    })
  end

  bench_config = [
    time: 1,
    warmup: 0.1,
    print: %{
      benchmarking: true,
      fast_warning: false,
      configuration: false,
      extended_statistics: true,
    },
  ]

end
