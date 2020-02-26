using System;
using System.Collections.Generic;

namespace International_Phonetic_Esoteric_Language {
	class Program {
		static void Main(string[] args) {

			Stack<Value> ValueStack = new Stack<Value>();

			for (int i = 0; i < 10; i++) {
				ValueStack.Push(new Value(i));
			}

			while (ValueStack.Count > 0) {
				Console.WriteLine(ValueStack.Pop().GetValue());
			}

		}
	}
}
