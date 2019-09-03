defmodule Benchmark do 

  def config do
    [
      time: 1,
      warmup: 0.1,
      print: %{
        benchmarking: true,
        fast_warning: false,
        configuration: false,
        extended_statistics: true,
      },
      formatters: [],
    ]
  end

  def compare(a, b, config) do
    Benchee.run(%{
      "compare_same" => fn -> ElixirCompare.nonconstant_compare(a, a) end,
      "compare_diff" => fn -> ElixirCompare.nonconstant_compare(a, b) end
    }, config).scenarios  |> Enum.map(fn stat -> %{min: stat.run_time_data.statistics.minimum, name: stat.name} end )
  end

  def compare_repeat(a, b, c, d, n, config) do
    IO.puts("Comparing strings: #{a}, #{b}, #{c}, #{d}.")
    Benchee.run(%{
      "compare_aa" => fn -> ElixirCompare.repeat_compare(a, a, n) end,
      "compare_ab" => fn -> ElixirCompare.repeat_compare(a, b, n) end,
      "compare_ac" => fn -> ElixirCompare.repeat_compare(a, c, n) end,
      "compare_ad" => fn -> ElixirCompare.repeat_compare(a, d, n) end,
    }, config).scenarios |> Enum.map(fn stat -> %{min: stat.run_time_data.statistics.minimum, name: stat.name} end )
  end

  def compare_firstlast(a, b, c, n, config) do
    IO.puts("Comparing strings: #{a} to #{b} and #{c}.")
    Benchee.run(%{
      "compare_ab" => fn -> ElixirCompare.repeat_compare(a, b, n) end,
      "compare_ac" => fn -> ElixirCompare.repeat_compare(a, c, n) end,
    }, config).scenarios |> Enum.map(fn stat -> %{min: stat.run_time_data.statistics.minimum, name: stat.name} end )
  end

end
