import {LetterTile} from "./LetterTile";

export class Guess {
  letterTiles: LetterTile[];

  constructor() {
      this.letterTiles = Array(5).fill(undefined).map(_ => new LetterTile());
  }
}

