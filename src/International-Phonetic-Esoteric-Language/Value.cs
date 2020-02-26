using System;

public class Value {
	private int Integer;
	private double Float;
	private string String;

	public Value(int Integer) {
		this.Integer = Integer;
	}

	public Value(float Float) {
		this.Float = Float;
	}

	public Value(string String) {
		this.String = String;
	}

	public dynamic GetValue() {
		if (Integer != default(int)) {
			return Integer;
		} else if (Float != default(float)) {
			return Float;
		} else if (String != default(string)) {
			return String;
		} else {
			return null;
		}
	}
}
