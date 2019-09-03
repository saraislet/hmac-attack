defmodule ElixirCompare do
  use Bitwise
  
  def nonconstant_compare(target, guess) when target == guess, do: :ok

  def nonconstant_compare(_target, _guess), do: :error

  def repeat_compare(target, guess, count) when count<=1 do
    nonconstant_compare(target, guess)
  end

  def repeat_compare(target, guess, count) do
    nonconstant_compare(target, guess)
    repeat_compare(target, guess, count - 1)
  end

  def repeat_constant_time_compare(target, guess, count) when count <= 1 do
    constant_time_compare(target, guess)
  end

  def repeat_constant_time_compare(target, guess, count) do
    constant_time_compare(target, guess)
    repeat_constant_time_compare(target, guess, count - 1)
  end

  # Call the private comparison function with no differences accumulated so far.
  def constant_time_compare(a, b) do
    constant_time_compare(a, b, 0)
  end

  # XOR the first bytes of the strings to get differences, OR with diff
  # to accumulate changes.
  defp constant_time_compare(<<firsta, resta::binary>>, <<firstb, restb::binary>>, diff) do
    constant_time_compare(resta, restb, diff ||| (firsta ^^^ firstb))
  end

  # End state: If both strings are empty and diff has not accumulated
  # any changed bits, the strings where equal, otherwise they are unequal.
  defp constant_time_compare(<<>>, <<>>, 0), do: :ok
  defp constant_time_compare(<<>>, <<>>, _diff), do: :error
  defp constant_time_compare(<<_, _::binary>>, <<>>, _diff), do: :error
  defp constant_time_compare(<<>>, <<_, _::binary>>, _diff), do: :error

end
