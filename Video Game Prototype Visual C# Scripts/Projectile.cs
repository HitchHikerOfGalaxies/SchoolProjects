using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Projectile : MonoBehaviour {

    [SerializeField] float speed = 5f;
    [SerializeField] bool moveLeft = true;


    Transform t;
    SpriteRenderer sr;

    // Use this for initialization
    void Awake()
    {
        t = GetComponent<Transform>();
        sr = GetComponent<SpriteRenderer>();
    }

    void Start () {
        FireLeft(moveLeft);
	}
	
	// Update is called once per frame
	void Update () {
		if (moveLeft)
        {
            t.Translate(Vector2.left * speed * Time.deltaTime);
        } else
        {
            t.Translate(Vector2.right * speed * Time.deltaTime);
        }
	}

    public void FireLeft(bool dir)
    {
        moveLeft = dir;
        if (!dir)
        {
            sr.flipX = true;
        }
    }
}
