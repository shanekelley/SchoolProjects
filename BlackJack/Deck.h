//
//  Deck.h
//  BlackJack
//
//  Created by Shane Kelley on 1/18/17.
//  Copyright © 2017 Shane Kelley. All rights reserved.
//
#include "Hand.h"
#ifndef Deck_h
#define Deck_h
class Deck: public Hand{        //create deck class
private:
    vector<Card> vecDeck;       //create deck vector
    int cardsRemaining;         //keep number of items in deck stored in variable

public:
    Deck();                     //default constructor
    void shuffle();             //put cards in deck in random order
    Card deal();                // return card from deck and remove that card
    void refill();              //clear cards in deck and refill it

    friend ostream& operator<<(ostream& d, Deck deck);  //overload function to output all cards
    
    
    
    
};

#endif /* Deck_h */
