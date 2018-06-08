using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class Player_UI : MonoBehaviour {

    private float timeLeft = 600;
    public int playerExp = 0;
    public GameObject timeLeftUI;
    public GameObject playerExpUI;

	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
        timeLeft -= Time.deltaTime;
        timeLeftUI.gameObject.GetComponent<Text>().text = ("Time Left: " + (int)timeLeft);
        playerExpUI.gameObject.GetComponent<Text>().text = ("Exp: " + playerExp);
        if (timeLeft < 0.1)
        {
            SceneManager.LoadScene("SampleScene");
        }
	}

    void OnTriggerEnter2D (Collider2D trig) //Once our player collides with the hitbox EndLevel you finish. Exp is collected based on time
    {
        Debug.Log("Touched the end of the level");
  //      CountExp();

    }

 //   void CountExp()
 //   {
  //      playerExp = playerExp + (int)(timeLeft * 10);
  //      Debug.Log(playerExp);
 //   }
}
