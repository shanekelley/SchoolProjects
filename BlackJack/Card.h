//
//  Card.h
//  
//
//  Created by Shane Kelley on 1/17/17.
//
//
#include <iostream>
#ifndef Card_h
#define Card_h
using namespace std;
enum Rank{Ace=1, Two,Three, Four, Five, Six, Seven, Eight, Nine, Ten, Jack, Queen, King};
enum Suit{Clubs, Diamonds, Spades, Hearts};     //create values for rank and suit
class Card
{
private:
    Rank rank;      //store value
    Suit suit;      //store suit
    
public:
    Card();                         //default constructor
    Card(Rank rank, Suit suit);     //copy constuctor to give card a rank and suit
    int getValue() const;           //return value of card
    char getSuit() const;           //return suit of card
    bool checkAce() const;           //check if card is an ace
    void setRank(Rank rank);        //set the rank of a card
    void setSuit(Suit suit);        //set the suit of a card
    friend ostream& operator<<(ostream& crd, Card card);    //overloaded fuction to output suit and rank
};

#endif /* Card_h */
