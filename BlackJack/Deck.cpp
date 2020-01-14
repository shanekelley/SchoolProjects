//
//  Deck.cpp
//  BlackJack
//
//  Created by Shane Kelley on 1/18/17.
//  Copyright © 2017 Shane Kelley. All rights reserved.
//
#include "Card.h"
#include "Hand.h"
#include "Deck.h"
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

Deck::Deck(){                       //default constructor
    Suit cardSuit;
    Rank cardRank;
    cardsRemaining = 52;
    for (int i = Clubs; i <= Hearts ; i++){     //nested for loops to create 52 cards each individual rank and suit
        for (int j = Ace; j <= King ; j++){
            if (i == Clubs)
                cardSuit = Clubs;
            else if (i == Diamonds)
                cardSuit = Diamonds;
            else if (i == Spades)
                cardSuit = Spades;
            else if (i == Hearts)
                cardSuit = Hearts;
            
            if (j == Ace)
                cardRank = Ace;
            else if (j == Two)
                cardRank = Two;
            else if (j == Three)
                cardRank = Three;
            else if (j == Four)
                cardRank = Four;
            else if (j == Five)
                cardRank = Five;
            else if (j == Six)
                cardRank = Six;
            else if (j == Seven)
                cardRank = Seven;
            else if (j == Eight)
                cardRank = Eight;
            else if (j == Nine)
                cardRank = Nine;
            else if (j == Ten)
                cardRank = Ten;
            else if (j == Jack)
                cardRank = Jack;
            else if (j == Queen)
                cardRank = Queen;
            else if (j == King)
                cardRank = King;
            vecDeck.push_back(Card(cardRank, cardSuit));    //put cards in deck
            
        };
    };
};

void Deck::shuffle(){               //shuffle the order of the cards
    random_shuffle(vecDeck.begin(), vecDeck.end());
};
Card Deck::deal(){
    int i = vecDeck.size() - 1;
    Card nextCard = vecDeck[i];     //get the card at the top of the deck to return
    vecDeck.pop_back();             //remove that card from the deck
    cardsRemaining -= 1;
    return nextCard;
    
};

ostream& operator<<(ostream& d, Deck deck){     //overloaded function to output all cards in deck
    int c = 0;
    for (int i = Clubs; i <= Hearts ; i++){
        for (int j = Ace; j <= King ; j++){
            cout << deck.vecDeck[c];
            c++;
        }
    }
    return d;
};

void Deck::refill(){
    this->clearHand();                          //delete all cards in deck to recreate them
    Suit cardSuit;
    Rank cardRank;
    cardsRemaining = 52;
    for (int i = Clubs; i <= Hearts ; i++){     //nested for loops to create 52 cards each individual rank and suit
        for (int j = Ace; j <= King ; j++){
            if (i == Clubs)
                cardSuit = Clubs;
            else if (i == Diamonds)
                cardSuit = Diamonds;
            else if (i == Spades)
                cardSuit = Spades;
            else if (i == Hearts)
                cardSuit = Hearts;
            
            if (j == Ace)
                cardRank = Ace;
            else if (j == Two)
                cardRank = Two;
            else if (j == Three)
                cardRank = Three;
            else if (j == Four)
                cardRank = Four;
            else if (j == Five)
                cardRank = Five;
            else if (j == Six)
                cardRank = Six;
            else if (j == Seven)
                cardRank = Seven;
            else if (j == Eight)
                cardRank = Eight;
            else if (j == Nine)
                cardRank = Nine;
            else if (j == Ten)
                cardRank = Ten;
            else if (j == Jack)
                cardRank = Jack;
            else if (j == Queen)
                cardRank = Queen;
            else if (j == King)
                cardRank = King;
            vecDeck.push_back(Card(cardRank, cardSuit));    //put cards in deck};
        };
    };
};
