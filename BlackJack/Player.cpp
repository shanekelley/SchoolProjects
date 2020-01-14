//
//  Player.cpp
//  BlackJack
//
//  Created by Shane Kelley on 1/23/17.
//  Copyright © 2017 Shane Kelley. All rights reserved.
//

#include "Player.h"
#include "Deck.h"
#include <iostream>
#include <vector>
using namespace std;

Player::Player(){                   //default constructor
    isBusted = false;
    turnDone = false;
};

int Player::stay(){
    int finalTotal = this->getTotal();          //set turnDone to true and return the players final total
    turnDone = true;
    return finalTotal;
};

void Player::hit(Deck d){                       //draw new hand and add it to player hand
    Card newCard = d.deal();
    this->addCard(newCard);
    if (this->getTotal() > 21) {                //check if the player hand is over 21
        isBusted = true;
        turnDone = true;
    };
};

bool Player::getIsBusted() const{               //check if isBusted is true
    bool bustedYN = isBusted;
    return bustedYN;
}
