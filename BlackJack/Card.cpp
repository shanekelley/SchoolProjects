//
//  Card.cpp
//  
//
//  Created by Shane Kelley on 1/17/17.
//
//

#include "Card.h"
#include <iostream>

Card::Card(){};                 //default constructor
Card::Card(Rank r, Suit s){     //copy constructor to chose what rank and suit
    rank = r;
    suit = s;
};
int Card::getValue() const{             //if statenents to take in a rank and return a value of that rank
    if ((rank == Ace) or (rank == 1))
        return 11;
    else if ((rank == Jack) or (rank == Queen) or (rank == King))
        return 10;
    else if (rank == Two)
        return 2;
    else if (rank == Three)
        return 3;
    else if (rank == Four)
        return 4;
    else if (rank == Five)
        return 5;
    else if (rank == Six)
        return 6;
    else if (rank == Seven)
        return 7;
    else if (rank == Eight)
        return 8;
    else if (rank == Nine)
        return 9;
    else if (rank == Ten)
        return 10;
    return 0;
};

void Card::setRank(Rank r){
    rank = r;
}

void Card::setSuit(Suit s){
    suit = s;
}
char Card::getSuit() const{
    if (suit == Clubs)
        return 'C';
    else if (suit == Diamonds)
        return 'D';
    else if (suit == Spades)
        return 'S';
    else
        return 'H';
};

bool Card::checkAce() const{            //check if the card is an ace
    if ((rank == Ace) or (rank == 1))
        return true;
    else
        return false;
    
};
ostream& operator<<(ostream& crd, Card card){   //overloaded function to output both value and suit
    cout << "[" << card.getValue() << card.getSuit() << "]" << endl;
    return crd;

}; this->
