//
//  BlackJackPlayer.cpp
//  BlackJack
//
//  Created by Shane Kelley on 1/23/17.
//  Copyright © 2017 Shane Kelley. All rights reserved.
//

#include "BlackJackPlayer.h"
#include <iostream>
#include <vector>
using namespace std;

BlackJackPlayer::BlackJackPlayer(){};       //default constructor
BlackJackPlayer::BlackJackPlayer(string name, int money){   //copy constructor
    BJPlayerName = name;
    isBusted = false;
    moneyLeft = money;
};

void BlackJackPlayer::bet(int num){ //set playersBet to input
    playersBet = num;
};

int BlackJackPlayer::getMoneyLeft() const{    //check how much the player has left
    int moneyL = moneyLeft;
    return moneyL;
};
    
void BlackJackPlayer::winLose(bool tf){ //add or take away money if player wins or loses
    if (tf == false) {
        moneyLeft -= playersBet;
    };
    if (tf == true){
        moneyLeft += playersBet;
    };
};

string BlackJackPlayer::getName() const{            // return players name
    return BJPlayerName;
};

int BlackJackPlayer::getBet() const{
    return playersBet;
}

