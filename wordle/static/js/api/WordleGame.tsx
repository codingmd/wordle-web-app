import {Guess} from "./Guess";

export class WordleGame {
  guesses: Guess[]; 

  constructor() {
      this.guesses = Array(6).fill(undefined).map(_ => new Guess());
  }
}
