defmodule ElixirCompare do
  @moduledoc """
  ElixirCompare keeps the contexts that define your domain
  and business logic.

  Contexts are also responsible for managing your data, regardless
  if it comes from the database, an external API or others.
  """
  
  def nonconstant_compare(target, guess) when target == guess, do: :ok

  def nonconstant_compare(_target, _guess), do: :error

  def repeat_compare(target, guess, count) when count<=1 do
    nonconstant_compare(target, guess)
  end

  def repeat_compare(target, guess, count) do
    nonconstant_compare(target, guess)
    repeat_compare(target, guess, count - 1)
  end

end

defmodule Benchmark do 

  def benchmark_compare(a, b) do
    Benchee.run(%{
      "compare_same" => fn -> ElixirCompare.nonconstant_compare(a, a) end,
      "compare_diff" => fn -> ElixirCompare.nonconstant_compare(a, b) end
    })
  end

  def benchmark_compare_repeat(a, b, n) do
    Benchee.run(%{
      "compare_same" => fn -> ElixirCompare.repeat_compare(a, a, n) end,
      "compare_diff" => fn -> ElixirCompare.repeat_compare(a, b, n) end
    })
  end

end